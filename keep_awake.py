import pyautogui
import time
from datetime import datetime

# delay between actions (in seconds)
DELAY = 60

try:
    print("Program is starting! Press Ctrl+C to stop")
    while True:
        # pressing virtual F15 key (doesn't exist on most keyboards)
        pyautogui.press('f15')
        current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        print(f"[{current_time}] Computer is awake")
        time.sleep(DELAY)

except KeyboardInterrupt:
    print("\nProgram stopped by user")
except Exception as e:
    print(f"\nError occurred: {str(e)}")