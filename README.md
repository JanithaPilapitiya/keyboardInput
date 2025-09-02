# Keystroke Logger

## 📖 Project Description
This is a simple **Python-based keystroke logging application** with a graphical user interface (GUI).  
It captures keyboard input in real-time, formats special keys (spaces, enters, backspaces, etc.), and saves the logged text to a file.  

The application can be run as a script or packaged into a standalone executable using **PyInstaller**.

---

## ✨ Features
- Real-time keystroke capture using the **pynput** library  
- Simple GUI with **Start/Stop** buttons using **tkinter**  
- Logs formatted keystrokes to `Files/keystrokes.txt`  
- Handles special keys: **space, enter, tab, backspace**  
- Ignores modifier keys (**Shift, Ctrl, Alt, etc.**)  
- Thread-safe logging with a **lock mechanism**  
- Automatic directory creation for log files  
- Compatible with both script and executable modes  

---

## 📦 Requirements
- **Python 3.x**  
- Dependencies:  
  - `pynput` (for keyboard listening)  
  - `tkinter` (usually included with Python, but ensure it's available)  

---

## ⚙️ Installation
1. Clone or download the project files.  
2. Install the required dependencies:
   ```bash
   pip install pynput
