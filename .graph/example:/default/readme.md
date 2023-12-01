# Default: test
https://gitlab.freedesktop.org/libinput/libei#high-level-summary
Quote:
>High-level summary
>Simple demo implementations for server and client are available in the [tools/](https://gitlab.freedesktop.org/libinput/libei/-/tree/main/tools) directory.
>The server starts a libeis context (which can be integrated with flatpak portals) and uses the libeis file descriptor to monitor for client requests.
>A client starts a libei context and connects to the server - either directly, via DBus or via a portal. The server (or the portal) approves or denies the client. After successful authentication the server sends one or more seats (a logical group of devices) to the client; the client can request the creation of devices with capabilities pointer, keyboard or touch, etc. in those seats.
>The client triggers input events on these devices, the server receives those as events through libeis and can forward them as if they were regular input events. The server has control of the client stream. If the stream is paused, events from the client are discarded. If the stream is resumed, the server will receive the events (but may discard them anyway depending on local state).
>The above caters for the xdotool use-case.
