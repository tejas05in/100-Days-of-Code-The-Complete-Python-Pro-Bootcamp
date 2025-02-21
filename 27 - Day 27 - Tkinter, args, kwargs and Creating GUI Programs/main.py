from tkinter import *


def button_clicked():
    # print(input_box.get())
    my_label.config(text=input_box.get())


window = Tk()
window.title("My First GUI Program")
window.minsize(500, 300)
window.config(padx=20, pady=20)


# label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# my_label.place(x=100, y=100)
# both below methods word for changing the text
# my_label["text"] = "New Text"
# my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

button2 = Button(text="New Button", command=button_clicked)
button2.grid(column=2, row=0)

# Entry
input_box = Entry(width=10)
input_box.grid(column=3, row=2)
print(input_box.get())


window.mainloop()

# do not mix up grid and pack method in the same program
