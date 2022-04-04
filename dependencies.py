
import subprocess
import sys
import time
from os import makedirs, path


def add_dependencies():
  """Add dependencies directory into path."""

  dependencies_path = get_dependencies_path()
  makedirs(dependencies_path, exist_ok=True)
  sys.path.insert(0, dependencies_path)

def get_dependencies_path():
  """Get path to dependencies directory. Here we will install and search for external modules."""

  deps_path = path.join(path.dirname(__file__), "dependencies")
  return path.abspath(deps_path)

def ensure_dependencies():
  """Make sure that dependencies which need installation are available. Install dependencies if needed."""

  tried = 0
  while tried < 3:
    tried = tried + 1
    try:
      import aiohttp
      return
    except:
      install_dependencies()

def install_dependencies():
  started = time.time()

  
  command = [sys.executable, '-m', 'ensurepip']
  result = subprocess.run(command, capture_output=True, text=True)
  print(f"PIP INSTALLATION:\ncommand {command} exited: {result.returncode},\nstdout: {result.stdout},\nstderr: {result.stderr}")

  requirements = path.join(path.dirname(__file__), 'requirements.txt')
  command = [sys.executable, '-m', 'pip', 'install', '--upgrade', '-t', get_dependencies_path(), '-r', requirements]
  result = subprocess.run(command, capture_output=True, text=True)
  print(f"AIOHTTP INSTALLATION:\ncommand {command} exited: {result.returncode},\nstdout: {result.stdout},\nstderr: {result.stderr}")
  print(f"Install finished in {time.time()-started}")
