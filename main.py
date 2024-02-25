import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

def upload_image():
    global original_image
    file_path = filedialog.askopenfilename()
    if file_path:
        original_image = cv2.imread(file_path)
        original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
        show_image(original_image)

def show_image(image):
    img = Image.fromarray(image)
    img.thumbnail((300, 300))
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.grid(row=1, column=0, padx=10, pady=10)

def convert_to_pencil_sketch():
    global pencil_sketch_image
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_RGB2GRAY)
    inverted_gray_image = 255 - gray_image
    blurred_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)
    pencil_sketch_image = cv2.divide(gray_image, 255 - blurred_image, scale=256)
    show_image(pencil_sketch_image)

def save_image():
    file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
    if file_path:
        cv2.imwrite(file_path, cv2.cvtColor(pencil_sketch_image, cv2.COLOR_RGB2BGR))

root = Tk()
root.title("Image to Pencil Sketch App")

upload_button = Button(root, text="Upload Image", command=upload_image)
upload_button.grid(row=0, column=0, padx=10, pady=10)

convert_button = Button(root, text="Convert", command=convert_to_pencil_sketch)
convert_button.grid(row=0, column=1, padx=10, pady=10)

save_button = Button(root, text="Save Image", command=save_image)
save_button.grid(row=0, column=2, padx=10, pady=10)

root.mainloop()
