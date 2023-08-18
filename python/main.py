from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

root = Tk()
# Name
root.title('maruv.sss')
# Размер 300 ширина 400 высота
root.geometry("400x400")
# Установка иконки
root.iconbitmap(default="logo_2.ico")
x = phonenumbers.parse("+442083661177", None)
print(x)


def error():
    message = messagebox.showinfo('⛔️ Error you fagges') * 10
    return message


def on_button_click():
    user_input = txt.get()
    number_1 = phonenumbers.parse(user_input)
    number_2 = geocoder.description_for_number(number_1, "ru")
    number_3 = carrier.name_for_number(number_1, "ru")
    result_label.config(text=f"{number_1}\n\n{number_2}\n\n{number_3}")


label = Label(text="Для того что бы отсканировать номер\nвведите его в таком формате: +380668679044",foreground="#A52A2A",font=("Arial Bold", 12)) # создаем текстовую метку
label.pack(pady=10)

txt = Entry(root, width=40)
txt.pack(anchor=S,pady=40)

result_label = Label(root, text="", font=40)
result_label.pack()

btn = ttk.Button(text="Scan", command=on_button_click)
btn.place(relx=0.5, rely=0.9, anchor=S, width=100, height=40)

# Позволяет не закрываться программе пока, пользователь этого не захочет
root.mainloop()
