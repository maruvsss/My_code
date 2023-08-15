from tkinter import *
from speedtest import Speedtest

root = Tk()
# Name
root.title('maruv.sss')
# Размер 300 ширина 400 высота
root.geometry("400x400")


def test():
    download = Speedtest().download()
    upload = Speedtest().upload()
    download_speed = round(download / (10 ** 6), 2)
    upload_speed = round(upload / (10 ** 6), 2)
    download_speed.config(text="Скорость загрузки:" + str(download_speed) +"MbPs")
    download_speed.config(text="Скорость отдачи:"+ str(upload_speed)+"MbPs")


button = Button(root, text='Начать', font=40, command=test)

download_label = Label(root, text='Скорость загрузки:', font=30)
download_label.pack(pady=(50, 0))
upload_label = Label(root, text='Скорость отдачи:', font=30)
upload_label.pack(pady=50)

button.pack(side=BOTTOM, pady=10)

# Позволяет не закрываться программе пока, пользователь этого не захочет
root.mainloop()
