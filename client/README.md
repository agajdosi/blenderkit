# BlenderKit-client

This a client for BlenderKit (previously daemon).
It's a local server that listens for requests from BlenderKit add-on and processes them.
Written in Go.

## How is it run
For now, the client is built for Windows, MacOS and Linux for both x86_64 and arm64.
BlenderKit-client binaries are shipped in the blenderkit.zip file, in /client directory where in repo source code is placed.
On add-on start, the client is copied into global_dir/client/bin/vX.Y.Z directory, and started.

## SystemTray
Pros:
- users see, client is running
- users could stop the client
- users could change settings of client outside Blender - this enables things for Godot

Cons:
- Linux binaries are bigger
- thus .zip file is bigger
- CGO has to be enabled (maybe problems with libraries on Linux? But hey, people can just install them)
- One have to install GCC compiler (https://github.com/FiloSottile/homebrew-musl-cross)

Needs to implement in dev.py -static flags so it runs on non musl linuxes:
```
CC=x86_64-linux-musl-gcc CGO_ENABLED=1 GOOS=linux GOARCH=amd64 go build -trimpath -ldflags "-extldflags -static"
```
