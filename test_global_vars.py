import unittest

import bpy


# Dynamically set the package context for the BlenderKit add-on
for addon in bpy.context.preferences.addons:
    if "blenderkit" in addon.module:
        __package__ = addon.module
        break

from . import global_vars


class TestVersions(unittest.TestCase):
    def test_client_version(self):
        """Client version in ./client/VERSION and in global_vars.CLIENT_VERSION must be the same."""
        with open("client/VERSION") as f:
            client_version = f.read().strip()
        self.assertEqual(
            global_vars.CLIENT_VERSION,
            f"v{client_version}",
            "global_vars.CLIENT_VERSION does not match the content of client/VERSION",
        )


class TestProductionIsSet(unittest.TestCase):
    def test_server_set_to_production(self):
        """Ensure the SERVER variable in global_vars is set to production."""
        expected_server = "https://www.blenderkit.com"
        self.assertEqual(
            global_vars.SERVER,
            expected_server,
            f"SERVER is not set to production. Expected: {expected_server}, Found: {global_vars.SERVER}",
        )
