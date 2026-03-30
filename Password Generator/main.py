import os
from tkinter import *
from random import randint
from PIL import Image, ImageTk

root=Tk()
root.title('Strong password generator')
icon_path = os.path.join(os.path.dirname(__file__), "icon.ico")

icon_path = os.path.join(os.path.dirname(__file__), "icon.png")
img = ImageTk.PhotoImage(file=icon_path)
root.iconphoto(False, img)
root.geometry("500x300")

my_password=chr(randint(32,126))

# generate random strong password
def new_rand():
    # clear our entry box
    pw_entry.delete(0,END)

    # get pw lenth and covert to integer
    try:
        pw_length = int(my_entry.get())
    except:
        pw_entry.delete(0, END)
        pw_entry.insert(0, "Enter a number!")
        return

    # create a variable to hold our password
    my_password=''

    # loop through password length 
    for x in range(pw_length):
        my_password+=chr(randint(32,126))

    # output password to the screen
    pw_entry.insert(0,my_password)


# copy to clipboard
def clipper():
    root.clipboard_clear()
    #copy to clipboard
    root.clipboard_append(pw_entry.get())


# Label Frame
lf=LabelFrame(root,text="How many characters")
lf.pack(pady=20)

# create entry box to Designate the number of characters
my_entry=Entry(lf,font=("Helvetica",24))
my_entry.pack(pady=20,padx=20)

# Entry box for our returned passsword
pw_entry=Entry(root,text='',font=("Helvetica",24))
pw_entry.pack(pady=20)

#create a frame for our buttons
my_frame=Frame(root)
my_frame.pack(pady=20)

# crate our buttons
my_button=Button(my_frame,text="Generator Strong Password",command=new_rand)
my_button.grid(row=0,column=0,padx=10)
 
clip_button=Button(my_frame,text="Copy to Clipboard",command=clipper)
clip_button.grid(row=0,column=1,padx=10)

root.mainloop()