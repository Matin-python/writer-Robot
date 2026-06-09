# PyAutoGUI Auto Typing Bot

This is a simple Python automation script built using the `PyAutoGUI` library.
The bot automatically types numbered motivational messages on your screen.

## Features

* Automatically types messages
* Adds numbering from 1 to 20
* Simulates keyboard typing and pressing Enter
* Includes typing delay for realistic behavior

## Code

```python
import pyautogui as robot

robot.sleep(3)

for i in range(1, 21):
    robot.sleep(0.5)
    robot.write(f'{i}. I can do it', interval=0.1)
    robot.press('enter')
```

## Requirements

Install Python and the required library:

```bash
pip install pyautogui
```

## How It Works

1. The script waits 3 seconds before starting.
2. It types:

   ```
   1. I can do it
   2. I can do it
   ...
   20. I can do it
   ```
3. After each line, it presses the Enter key automatically.

## How to Run

Run the script using:

```bash
python writer.py
```

Make sure your cursor is focused on a text field (like Notepad, VS Code, or a chat box) before the 3-second timer ends.

## Example Use Cases

* Typing practice automation
* Simple desktop automation
* Learning Python automation
* Fun keyboard bot projects

## Warning

This script controls your keyboard automatically.
Do not move focus away from the target window while the script is running.

## License

This project is open-source and free to use.


## Author

    Mohammad Reza Bakhshandeh
    Electrical Engineering Graduate | Python Learner
    Interested in AI and Problem Solving
