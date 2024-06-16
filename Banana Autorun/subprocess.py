import subprocess
import time
import os
import customtkinter
from threading import Thread

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
icon = os.path.join(BASE_DIR, 'icon.ico')
path = os.path.join(BASE_DIR, 'Banana.exe')

banana_autorun = customtkinter.CTk()
banana_autorun.resizable(width=False, height=True)
banana_autorun.title('banana_autorun')
banana_autorun.minsize(150,0)
banana_autorun.maxsize(150,50)
banana_autorun.iconbitmap(icon)
customtkinter.set_appearance_mode('dark') 

run_button = customtkinter.CTkButton(banana_autorun, text='Run', command=lambda: Thread(target=autorunBanana, daemon=True).start())
run_button.pack()
info_label = customtkinter.CTkLabel(banana_autorun, text='')
info_label.pack()

startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
startupinfo.wShowWindow = subprocess.SW_HIDE

def autorunBanana():
    info_label.configure(text = 'Started')
    subprocess.Popen(path)
    time.sleep(90)
    os.system('taskkill /f /im banana.exe')
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
    autorunBanana()

banana_autorun.mainloop()