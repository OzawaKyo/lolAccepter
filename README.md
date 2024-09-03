# Auto Clicker and Image Detection Project

This project contains scripts for automating mouse clicks and detecting images on the screen. It is useful for tasks such as automatically accepting game invites or clicking buttons on the screen.

### Files

- **button_clicker.py**: Contains a script to detect a button on the screen and click it.
- **image_detecter.py**: Continuously scans the screen for a specific image and prints its location if found.
- **lol_accpeter.py**: Specifically designed to detect and accept game invites by clicking on the "accept" button.
- **mouse_position.py**: Displays the current mouse position on the screen .

## Dependencies

- `pyautogui` 
- `keyboard`
- `win32api`
- `win32con`
- `time`
- `random`

You can install the required dependencies using pip:

```sh
pip install pyautogui keyboard pywin32
```
## Usage

button_clicker.py

This script detects a button on the screen and clicks it.
```sh
python button_clicker.py
```

image_detecter.py

This script continuously scans the screen for an image named accept.png and prints its location if found.
```sh
python image_detecter.py
```

lol_accpeter.py

This script detects and accepts game invites by clicking on the "accept" button.
```sh
python lol_accpeter.py
```
mouse_position.py

This script displays the current mouse position on the screen.
```sh
python mouse_position.py
```

Good Game Have Fun! ```
