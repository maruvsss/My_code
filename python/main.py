from tkinter import *
from tkinter import ttk
from speedtest import Speedtest
import time

elapsed_time = time.time()
def test():
    text_main.config(text="Результаты теста")
    download = Speedtest().download()
    upload = Speedtest().upload()
    download_speed = round(download / (10 ** 6), 2)
    upload_speed = round(upload / (10 ** 6), 2)

    download_label.config(text="Скорость загрузки: " + str(download_speed) + "MbPs")
    upload_label.config(text="Скорость отдачи: " + str(upload_speed) + "MbPs")


root = Tk()
# Name
root.title('maruv.sss')
# Размер 300 ширина 400 высота
root.geometry("400x400")
# Установка иконки
root.iconbitmap(default="logo_2.ico")
button = ttk.Button(root, text='Начать', command=test)
text_main = Label(root, text='maruv.sss', font=("Arial", 14),foreground="#B71C1C")
text_main.pack()


download_label = Label(root, text='Скорость загрузки: ', font=30)
download_label.pack(pady=(50, 0))
upload_label = Label(root, text='Скорость отдачи: ', font=30)
upload_label.pack(pady=10)

button.pack(anchor='center', expand=True, ipadx=10, ipady=10)

# Позволяет не закрываться программе пока, пользователь этого не захочет
root.mainloop()
