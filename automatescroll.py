import pyautogui
import sys
import time
import subprocess

print('Press Ctrl-C to quit.')
try:
    start_time = time.time()
    while True:
        pyautogui.scroll(-10)  # scroll down 10 "clicks"
        time.sleep(1)

        # Check if 15 minutes have elapsed
        elapsed_time = time.time() - start_time
        if elapsed_time >= 900:  # 15 minutes in seconds
            # Lock the computer (assuming Windows OS, you may need to adjust for other OS)
            subprocess.run(["rundll32.exe", "user32.dll,LockWorkStation"])
            break

except KeyboardInterrupt:
    print('\n')
