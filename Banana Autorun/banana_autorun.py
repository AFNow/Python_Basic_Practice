import subprocess
import time
import os
import customtkinter
from threading import Thread

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#icon = os.path.join(BASE_DIR, 'icon.ico')
path = os.path.join(BASE_DIR, 'steam.exe -applaunch 2923300')

banana_autorun = customtkinter.CTk()
banana_autorun.resizable(width=False, height=True)
banana_autorun.title('banana_autorun')
banana_autorun.minsize(150,0)
banana_autorun.maxsize(150,50)
#banana_autorun.iconbitmap(icon)
customtkinter.set_appearance_mode('dark') 

run_button = customtkinter.CTkButton(banana_autorun, text='Run', command=lambda: Thread(target=autorun_banana, daemon=True).start())
run_button.pack()
info_label = customtkinter.CTkLabel(banana_autorun, text='')
info_label.pack()


def autorun_banana():
    try:
        app = subprocess.Popen(path)
        info_label.configure(text = 'Started')
        time.sleep(90)
        os.system('taskkill /f /im banana.exe')
        app.kill()
        info_label.configure(text = 'Killed')
        time.sleep(5)
        info_label.configure(text = 'Waiting 3 hours')
        time.sleep(3600)
        info_label.configure(text = 'Waiting 2 hours')
        time.sleep(3600)
        info_label.configure(text = 'Waiting 1 hour')
        time.sleep(1800)
        info_label.configure(text = 'Waiting 30 minutes')
        time.sleep(1200)
        info_label.configure(text = 'Waiting 10 minutes')
        time.sleep(600)
        autorun_banana()
    except:
        info_label.configure(text = 'No Banana.exe found')
        time.sleep(5)
        info_label.configure(text = BASE_DIR)
banana_autorun.mainloop()