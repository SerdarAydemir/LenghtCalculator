import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
import os, sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

window = tk.Tk()
window.title("Omvang Rekenmachine")
window.geometry("600x400")
window.resizable(False, False)
image_original = Image.open(resource_path('Images/arc.png'))
image_tk = ImageTk.PhotoImage(image_original)


def berekenen():
    s1 = int(entstandaarddoos.get() or 0)
    s2 = int(ent182doos.get() or 0)
    s3 = int(ent183doos.get() or 0)
    s4 = int(ent402doos.get() or 0)
    s5 = 0.125
    s6 = 0.15625
    s7 = 0.3125
    s8 = s1 * s5
    s9 = s2 * s6
    s10 = s3 * s7
    s11 = s4 * s7
    s12 = float(s8) + float(s9) + float(s10) + float(s11)
    lbltotaalomvang2['text'] = f"De totaal omvang is {s12} meters."

def nieuwe_berekenen():
    entstandaarddoos.delete(0,'end')
    ent182doos.delete(0,'end')
    ent183doos.delete(0,'end')
    ent402doos.delete(0,'end')
    lbltotaalomvang2.config(text = "")

    

labelbackground = ttk.Label(window, image=image_tk)
labelbackground.place(x=0, y=0)
labelbackground.pack()

lblheader = tk.Label(window, text="Omvang Rekenmachine", 
                  font="CourrierNew 16 bold", bg = "black", fg = "white" )
lblheader.place(x=200, y=40)

lbldoostype = tk.Label(window, text= "Doos Type", font="CourrierNew 12 bold",bg = "black", fg = "white")
lbldoostype.place(x=180, y=100)

lblaantaldozen = tk.Label(window, text= "Aantal Dozen", font="CourrierNew 12 bold",bg = "black", fg = "white")
lblaantaldozen.place(x=355, y=100)

lblstandaarddoos = tk.Label(window, text= "169 (Standaard Doos) =", font="CourrierNew 11 bold",bg = "black", fg = "white")
lblstandaarddoos.place(x=150, y=130)

lbl182doos = tk.Label(window, text= "182 =", font="CourrierNew 11 bold",bg = "black", fg = "white")
lbl182doos.place(x=150, y=160)

lbl183doos = tk.Label(window, text= "183 =", font="CourrierNew 11 bold",bg = "black", fg = "white")
lbl183doos.place(x=150, y=190)

lbl402doos = tk.Label(window, text= "402 =", font="CourrierNew 11 bold",bg = "black", fg = "white")
lbl402doos.place(x=150, y=220)

lbltotaalomvang = tk.Label(window, text= "Totaal Omvang =", font="CourrierNew 12 bold",bg = "black", fg = "white")
lbltotaalomvang.place(x=150, y=300)

entstandaarddoos = tk.Entry(window, font="CorrierNew 11 bold")
entstandaarddoos.place(x=325, y=130)

ent182doos = tk.Entry(window, font="CorrierNew 11 bold")
ent182doos.place(x=325, y=160)

ent183doos = tk.Entry(window, font="CorrierNew 11 bold")
ent183doos.place(x=325, y=190)

ent402doos = tk.Entry(window, font="CorrierNew 11 bold")
ent402doos.place(x=325, y=220)

lbltotaalomvang2 = tk.Label(window, font="CorrierNew 11 bold")
lbltotaalomvang2.place(x=300, y=300)

btnberekenen = tk.Button(window, text="Berekenen", font="CourrierNew 10 bold",bg = "black", fg = "white", command=berekenen)
btnberekenen.place(x=180,y=260)

btnnieuweberekenen = tk.Button(window, text="Nieuwe Berekenen", font="CourrierNew 10 bold",bg = "black", fg = "white", command = nieuwe_berekenen)
btnnieuweberekenen.place(x=355,y=260)

window.mainloop()