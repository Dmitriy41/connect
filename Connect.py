from tkinter import *
import netifaces
import os
import subprocess
import time
from tkinter import messagebox as mb
from threading import Thread


def GO():
    while 1:
        IP = txt.get()
        ping = subprocess.check_output(["ping", "-c","1", str(IP)])
        if ping == 0:
            status_text.insert(0.1, str(IP) + " active" + "\n")

        else:
            status_text.insert(0.1, str(IP) + " inactive" + "\n")
            os.system("networksetup -setairportpower airport on")

        time.sleep(1)


root = Tk()


def click():
    go = Thread(target=GO)
    go.start()


root.title("Connect")
root.geometry("500x200")
lbl1 = Label(text="IP Клиента:")
txt = Entry()

lbl2 = Label(text="Статус соединения:")
lbl3 = Label(text="Ethernet:")
lbl4 = Label(text="WI-FI:")
lbl5 = Label(text="")
lbl6 = Label(text="")
btn = Button(text="Сканировать", command=click)
lbl7 = Label(text="Статус:")
status_text = Text(height=5, width=25)

lbl1.place(x=10, y=10)
txt.place(x=10, y=30)
lbl2.place(y=10, x=320)
lbl3.place(x=320, y=40)
lbl4.place(x=320, y=70)
lbl5.place(x=390, y=40)
lbl6.place(x=390, y=70)
lbl7.place(x=10, y=60)
btn.place(x=320, y=150)
status_text.place(x=10, y=85)

try:
    def_gw_device = netifaces.gateways()['default'][netifaces.AF_INET][1]
    if def_gw_device == "en0":
        lbl6.config(text="OK", fg="green")
    else:
        lbl6.config(text="")
        lbl5.config(text="OK", fg="green")
except Warning:
    mb.showerror(title="Не найден сетевой интерфейс", message="Подключите ваш компьютер к сети(WI-FI, Ethernet)")
root.mainloop()
