import pyautogui
import win32api, win32con
import keyboard
import time

# THIS REMOVES THE DEFAULT 0.1s LIMIT
pyautogui.PAUSE = 0

clicking = False
delay = 0.001  # Starting at 1ms

print("--- Extreme Speed Auto-Clicker ---")
print("S: Start/Stop | Up: Faster | Down: Slower | Q: Quit")

def click_action():
    # Direct OS calls for max speed
    x, y = win32api.GetCursorPos()
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

while True:
    # Toggle Start/Stop
    if keyboard.is_pressed('s'):
        clicking = not clicking
        print(f"Status: {'CLICKING' if clicking else 'STOPPED'}")
        time.sleep(0.2)

    # Adjust Speed (Tiny increments for high speed)
    if keyboard.is_pressed('up'):
        delay = max(0.0, delay - 0.001)
        print(f"Delay: {delay:.4f}s")
        time.sleep(0.05)
        
    if keyboard.is_pressed('down'):
        delay += 0.001
        print(f"Delay: {delay:.4f}s")
        time.sleep(0.05)


    # Click Loop
    if clicking:
        click_action()
        if delay > 0:
            time.sleep(delay)

    if keyboard.is_pressed('q'):
        break