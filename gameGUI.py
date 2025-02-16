from tkinter import *
from PIL import Image, ImageTk

#window = Tk()
#window.title("Game Screen")
#window.geometry("700x700")

#w = Label(window, text="Welcome!", font=("Arial", 40, "bold"), height=2, width=30, fg="pink", bg="green")
#w.pack()

start = Tk()
start.title("Start Screen")
start.geometry("300x300")

def close_window():
    start.destroy()

button = Button(start, text='Play', font=("Arial", 40, "bold"), width=25, fg="black", command=close_window)
button.pack()

start.mainloop()



#img = Image.open(r"C:\Users\sriya\Downloads\Grid.jpg")

#img_resized = img.resize((700, 700))

#img_tk = ImageTk.PhotoImage(img_resized)

#label = Label(window, image=img_tk)
#label.pack()

#label.image = img_tk

#window.mainloop()