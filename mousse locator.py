import pyautogui

while True:
    x, y = pyautogui.position()
    print(f"Position de la souris: X={x} Y={y}")