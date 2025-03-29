# Simple Keylogger with Active Window Tracking (Windows)

This is a basic educational keylogger script written in Python.  
It logs all keystrokes and shows the title of the active window (e.g., Chrome, Notepad) whenever it changes.

> ⚠️ **For educational purposes only.**  
> Do not use this script on any computer or system without proper permission.

---

## 💻 Features
- Records every key pressed.
- Detects and logs the active window title when changed.
- Inserts a new line after every 50 characters to keep the log readable.

---

## 🧰 Requirements

- Python 3.x  
- `pynput`  
- `pywin32`

Install dependencies:

```bash
pip install pynput pywin32
