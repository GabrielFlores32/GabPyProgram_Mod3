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

#result box
main_entry = customtkinter.CTkEntry(app, width=280, height=50)
main_entry.place(x=10, y=10)










app.mainloop()

