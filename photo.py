from tkinter import *
from PIL import Image, ImageChops

win = Tk()
win.title("Spot the differences...!!!")
win.geometry("500x500")
win.config(bg="black")
win.iconbitmap("jk.ico")


def spot():
    img1 = Image.open(E1.get())
    img2 = Image.open(E2.get())

    difference = ImageChops.difference(img1, img2)
    if difference.getbbox():
        difference.show()


def nextpage():
    win1 = Toplevel()
    win1.geometry("500x500")
    win1.title("Image Input")
    win1.config(bg="black")
    win1.iconbitmap("jk.ico")

    global E1
    global E2

    L1 = Label(win1, text="Image1 Filename : ", bg="black", fg="white", font=("Helvetica", 15, "bold italic"))
    L1.grid(row=0, column=0, pady=(200, 30), padx=(40, 20))
    L1 = Label(win1, text="Image2 Filename : ", bg="black", fg="white", font=("Helvetica", 15, "bold italic"))
    L1.grid(row=1, column=0, pady=(0, 30), padx=(40, 20))
    E1 = Entry(win1)
    E1.grid(row=0, column=1, pady=(200, 30), ipadx=50)
    E2 = Entry(win1)
    E2.grid(row=1, column=1, pady=(0, 30), ipadx=50)
    Button(win1, text="Images Uploaded...!!!", command=spot).grid(row=2, column=0, columnspan=2, ipadx=80, padx=80)


Label(win, text="GUI for Spotting Differences", bg="black", fg="white", font=("Helvetica", 20, "bold italic")).pack(pady=(200,20))
Button(win, text="Get Started", command= nextpage).pack(ipadx=120)

win.mainloop()
