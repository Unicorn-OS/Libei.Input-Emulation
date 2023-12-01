# Modifier Key
https://gitlab.freedesktop.org/libinput/libei#differences-between-xtest-vs-libei

Quote:
>One example is xdotool which does window focus and modifier mangling (see below). Window focus notification is not available to a pure libei client and would have to be obtained or handled on a separate channel, e.g. X or Wayland. Having said that, a Wayland client does not usually have acess to query or modifiy the window focus.
>
>Modifiers in xdotool are handled by obtaining the modifier mask from the X server, identifying any difference to the intended mask and emulating key events to change the modifier state to the intended one. For example, if capslock is on, xdotool would send a capslock key event first (thus disabling capslock) and then the actual key sequence. This is followed by another capslock key event to restore the modifier mask.
>
>This is not possible for a pure libei client as the modifier state is maintained by the windowing system (if any). A client can obtain the modifier state on Wayland on wl_keyboard.enter but when the client is in-focus, there is rarely a need to emulate events.
