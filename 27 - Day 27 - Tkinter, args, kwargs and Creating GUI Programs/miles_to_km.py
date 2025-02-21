from tkinter import *


def button_clicked():
    miles = float(entry.get())
    km = round(miles * 1.60934)
    ans.config(text=km)


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# TEXT
entry = Entry(width=10, justify=CENTER)
entry.grid(row=0, column=1)

label_1 = Label(text="Miles")
label_1.grid(row=0, column=2)

label_2 = Label(text="is equal to")
label_2.grid(row=1, column=0)

ans = Label(text=0)
ans.grid(row=1, column=1)

label_3 = Label(text="Km")
label_3.grid(row=1, column=2)

button = Button(text="Calculate", command=button_clicked)
button.grid(row=2, column=1)
window.mainloop()
