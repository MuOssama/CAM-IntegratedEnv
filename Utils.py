from tkinter import *
from PIL import Image, ImageTk

def clear_widgets(root):
    #this function deletes all what on the screen
    for widget in root.winfo_children():
        widget.destroy()
