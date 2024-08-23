from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os

image_reference = None

def showimage():
    global image_reference
    try:
        filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Show image file", filetypes=(("JPG File", "*.jpg"), ("PNG file", "*.png"), ("All files", "*.*")))
        if filename:
            img = Image.open(filename)
            img.thumbnail((400, 400))  # Resize image to fit within 400x400
            img = ImageTk.PhotoImage(img)
            ibl.configure(image=img)
            ibl.image = img
            image_reference = img
    except Exception as e:
        print(f"Error loading image: {e}")

root = Tk()

fram = Frame(root)
fram.pack(side=BOTTOM, padx=15, pady=15)

ibl = Label(root)
ibl.pack()

btn = Button(fram, text="Select Image", command=showimage)
btn.pack(side=tk.LEFT)

btn2 = Button(fram, text="Exit", command=root.destroy)
btn2.pack(side=tk.LEFT, padx=12)

root.title("Image Viewer")
root.geometry("400x450")
root.mainloop()
