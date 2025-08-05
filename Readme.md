# Simple Auto Clicker

## Description

This is a simple auto-clicker application with a graphical user interface (GUI) built using Python and Tkinter. It allows users to automate mouse clicks at a specified interval. The application is designed to be straightforward and easy to use.

## Features

- **User-Friendly GUI:** A clean and simple interface for easy operation.
- **Customizable Click Interval:** Set the time between clicks in minutes. You can use decimal values for shorter intervals (e.g., 0.5 for 30 seconds).
- **Quick Set Buttons:** Quickly set the interval to common values: 30 seconds, 1 minute, 2 minutes, or 5 minutes.
- **Start/Stop Control:** Easily start and stop the auto-clicking process.
- **Status Display:** Provides real-time feedback on the application's status (e.g., ready, clicking, stopped) and the number of clicks performed.
- **Background Operation:** The clicking process runs in a separate thread, so the GUI remains responsive.
- **Clicks at Current Mouse Position:** The application clicks at the current location of the mouse pointer without moving it.

## Requirements

- Python 3
- `pynput` library

You can install the required library using pip:
```
pip install pynput
```
Note: `tkinter` is usually included with standard Python installations.

## How to Run the Application

1.  Make sure you have Python 3 and `pynput` installed.
2.  Save the code as `main.py`.
3.  Open a terminal or command prompt.
4.  Navigate to the directory where you saved `main.py`.
5.  Run the following command:
    ```
    python main.py
    ```

## How to Use the Auto Clicker

1.  **Run the application** using the command above.
2.  **Position your mouse cursor** at the location on the screen where you want the clicks to occur.
3.  **Set the click interval** by typing a number in the "Click every" box. The value is in minutes.
4.  **Click the START button.** The application will begin clicking at the set interval at your mouse's current position.
    - **Important:** Do not move the mouse after starting, as the clicks will happen wherever the pointer is.
5.  **Click the STOP button** to cease the clicking process at any time.

---
This `Readme.txt` was generated based on the `main.py` script.
