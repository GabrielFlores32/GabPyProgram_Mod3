#create a simple calculator app
#adding the calcualtor app to a customtkinter

import customtkinter
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox

#gui theme
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

#size of the window
app = customtkinter.CTk()
app.title("simple calculator app") 
app.geometry("300x300") 


def button_click(number):
    main_entry.insert(END,number)

def clear():
    main_entry.delete(0,END)
    
def calculate():
    try:
        equation = main_entry.get()
        new_equation = equation.replace("X", "*")
        result = eval(new_equation)
        clear()
        main_entry.insert(0,result)
    except ZeroDivisionError:
        messagebox.showerror("ERROR", "0 cannot be devided")
    else:
        messagebox.showerror("ERROR", "please enter valid values")
  
        
#result box
main_entry = customtkinter.CTkEntry(app, width=280, height=50)
main_entry.place(x=10, y=10)
    
#buttons function
number1_button = customtkinter.CTkButton(app, text="1", command=lambda: button_click("1"), width=60)
number1_button.place(x=10, y=170)

number2_button = customtkinter.CTkButton(app, text="2", command=lambda: button_click("2"), width=60)
number2_button.place(x=80, y=170)

number3_button = customtkinter.CTkButton(app, text="3", command=lambda: button_click("3"), width=60)
number3_button.place(x=150, y=170)

number4_button = customtkinter.CTkButton(app, text="4", command=lambda: button_click("4"), width=60)
number4_button.place(x=10, y=125)

number5_button = customtkinter.CTkButton(app, text="5", command=lambda: button_click("5"), width=60)
number5_button.place(x=80, y=125)

number6_button = customtkinter.CTkButton(app, text="6", command=lambda: button_click("6"), width=60)
number6_button.place(x=150, y=125)

number7_button = customtkinter.CTkButton(app, text="7", command=lambda: button_click("7"), width=60)
number7_button.place(x=10, y=80)

number8_button = customtkinter.CTkButton(app, text="8", command=lambda: button_click("8"), width=60)
number8_button.place(x=80, y=80)

number9_button = customtkinter.CTkButton(app, text="9", command=lambda: button_click("9"), width=60)
number9_button.place(x=150, y=80)

number0_button = customtkinter.CTkButton(app, text="0", command=lambda: button_click("0"), width=60)
number0_button.place(x=10, y=215)

dot_button = customtkinter.CTkButton(app, text=".", command=lambda: button_click("."), width=60)
dot_button.place(x=80, y=215)

calculate_button = customtkinter.CTkButton(app, command=calculate, text="=",  width=270)
calculate_button.place(x=10, y=255)

addition_button = customtkinter.CTkButton(app, text="+", command=lambda: button_click("+"), width=60)
addition_button.place(x=220, y=80)

subtraction_button = customtkinter.CTkButton(app, text="-", command=lambda: button_click("-"), width=60)
subtraction_button.place(x=220, y=125)

multiplication_button = customtkinter.CTkButton(app, text="X", command=lambda: button_click("X"), width=60)
multiplication_button.place(x=220, y=170)

division_button = customtkinter.CTkButton(app, text="/", command=lambda: button_click("/"), width=60)
division_button.place(x=220, y=215)

clear_button = customtkinter.CTkButton(app, text="C", command=clear,  width=60)
clear_button.place(x=150, y=215)










app.mainloop()

