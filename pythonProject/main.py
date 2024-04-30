from tkinter import *
from tkinter import filedialog
import tkinter as tk

root = tk.Tk()
root.geometry("200x200")


def encrypt_image():
    file1 = filedialog.askopenfile(mode='r')
    if file1 is not None:
        file_name = file1.name
        key = entry1.get(1.0, END)
        fi = open(file_name, 'rb')
        image = fi.read()
        fi.close()
        image = bytearray(image)
        for index, values in enumerate(image):
            image[index] = values ^ int(key)
        fi1 = open(file_name, 'wb')
        fi1.write(image)
        fi1.close()


b1 = Button(root, text="encrypt", command=encrypt_image)
b1.pack()

entry1 = Text(root, height=1, width=10)
entry1.pack()

root.mainloop()
