# Import required packages
from tkinter import *
from tkinter import filedialog
import os
import tkinter as tk
import cv2
import pytesseract as tess

# Mention the installed location of Tesseract-OCR in your system
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to extract text from image
def img2txt():
    # Browse and select the image file.
    selected_img = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", filetype=(("JPG file", "*.jpg"), ("PNG file", "*.png"), ("All Files", "*.*")))

    # Acknowledgement displayed in terminal
    print("Process Started")
    i2t_text.delete("1.0", "end")
    img = cv2.imread(selected_img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Creating text file
    file = open("Output.txt", "w+")

    # Extracted text is written in txt file
    text = tess.image_to_string(img)
    for statement in range(0,len(text)-1):
        file.write(text[statement])

    file.write('\n[Given image text is Extracted]')
    file.close()

    # Txt file is displayed in textbox
    file = open("Output.txt")
    stuff = file.read()
    i2t_text.insert(END, stuff)
    file.close()

    # Acknowledgement displayed in terminal
    print("Process Completed")

# User Interface part - Tkinter

# Window for User Interface
ui = Tk()

# Creating a frame
frame = Frame(ui)
frame.pack(side=BOTTOM, padx=15, pady=15)

# Creating scrollbar
scroll = Scrollbar(ui)
scroll.pack(side=RIGHT, fill=Y)

# Creating a Text Box
i2t_text = Text(ui, wrap=NONE, width=80, height=45, font=("Arial", 16), yscrollcommand=scroll.set)
i2t_text.pack(pady=10)

# Creating a Label
lbl = Label(ui)
lbl.pack()


# Creating a button 1 for browse image
btn1 = Button(frame, text="Browse Image", command=img2txt, bg='black', fg='white')
btn1.pack(side=tk.LEFT)

# Creating a button 2 for exit function
btn2 = Button(frame, text="Exit", command = lambda : exit(), bg='black', fg='white')
btn2.pack(side=tk.LEFT, padx=10)

# Executing the program
if __name__ == "__main__":
    ui.title("Image2Text")
    frame.config(bg ='gray')
    ui.config(bg = 'gray')
    ui.geometry("1280x720")
    scroll.config(command=i2t_text.yview)
    ui.mainloop()

