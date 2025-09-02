Keystroke Logger
Project Description
This is a simple Python-based keystroke logging application with a graphical user interface (GUI). It captures keyboard input in real-time, formats special keys (spaces, enters, backspaces, etc.), and saves the logged text to a file. The application is designed to run as a script or be packaged into a standalone executable using PyInstaller.

Features
Real-time keystroke capture using the pynput library
Simple GUI with Start/Stop buttons using tkinter
Logs formatted keystrokes to Files/keystrokes.txt
Handles special keys like space, enter, tab, and backspace
Ignores modifier keys (Shift, Ctrl, Alt, etc.)
Thread-safe logging with a lock mechanism
Automatic directory creation for log files
Compatible with both script and executable modes
Requirements
Python 3.x
Dependencies:
pynput (for keyboard listening)
tkinter (usually included with Python, but ensure it's available)
Installation
Clone or download the project files.
Install the required dependencies:

pip install pynput
Note: tkinter is typically included with Python installations. If not, install it via your system's package manager (e.g., sudo apt-get install python3-tk on Ubuntu).
Usage
Running as a Script
Navigate to the project directory.
Run the script:

python logger.py
The GUI window will appear.
Click "Start" to begin logging keystrokes.
Click "Stop" to end logging and save the keystrokes to Files/keystrokes.txt.
The log file will be appended with each stop action.
Running the Executable
Build the executable first (see Building Executable section).
Run the generated logger.exe (or logger on Linux/Mac).
Follow the same GUI steps as above.
Building Executable
To create a standalone executable using PyInstaller:

Install PyInstaller:

pip install pyinstaller
Run the build command:

pyinstaller logger.spec
The executable will be created in the dist/ directory.
Note: The logger.spec file is already configured for this project.

Sample Output
The logged keystrokes are saved in plain text format. Example content from Files/keystrokes.txt:


word

Hi, I',m Janitha
This represents typed text including spaces and newlines.
