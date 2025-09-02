from pynput import keyboard
import os
import threading
import tkinter as tk
from tkinter import messagebox
import sys

# Determine base path (whether script or executable)
if getattr(sys, 'frozen', False):
    base_path = os.path.dirname(sys.executable)
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

# Set up log directory and file
files_dir = os.path.join(base_path, 'Files')
os.makedirs(files_dir, exist_ok=True)
log_path = os.path.join(files_dir, 'keystrokes.txt')

keystrokes = []
lock = threading.Lock()
listener = None

def format_key(key):
    try:
        if hasattr(key, 'char') and key.char:
            return key.char
        elif key == keyboard.Key.space:
            return ' '
        elif key == keyboard.Key.enter:
            return '\n'
        elif key == keyboard.Key.tab:
            return '\t'
        elif key == keyboard.Key.backspace:
            return '[BACKSPACE]'
        else:
            # Ignore modifier keys like Shift, Ctrl, Alt, etc.
            return ''
    except:
        return ''


def on_press(key):
    with lock:
        keystrokes.append(format_key(key))

def start_logging():
    global listener
    if listener is None or not listener.running:
        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        status_label.config(text="Recording...")

def stop_logging():
    global listener
    if listener:
        listener.stop()
        listener.join()
    with lock:
        if keystrokes:
            with open(log_path, "a", encoding="utf-8") as f:
                f.write(''.join(keystrokes))
            keystrokes.clear()
    status_label.config(text="Recording stopped.")
    messagebox.showinfo("Logger", f"Keystrokes saved to:\n{log_path}")

# GUI setup
window = tk.Tk()
window.title("Keystroke Logger")
window.geometry("300x150")
window.resizable(False, False)

tk.Label(window, text="Keystroke Logger", font=("Arial", 14)).pack(pady=10)

status_label = tk.Label(window, text="Idle", fg="gray")
status_label.pack(pady=5)

tk.Button(window, text="Start", width=10, command=start_logging).pack(pady=2)
tk.Button(window, text="Stop", width=10, command=stop_logging).pack(pady=2)

window.mainloop()
