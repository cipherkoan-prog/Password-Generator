import os
from tkinter import *
from tkinter import messagebox
from random import randint
from PIL import Image, ImageTk
import json

FILE_NAME="password.json"

def load_password():
    try:
        with open(FILE_NAME, "r")as file:
            return json.load(file)
    except:
        return{}
    
def save_password():
    website=website_entry.get()
    username=username_entry.get()
    password=pw_entry.get()

    if website =="" or username =="" or password =="":
        messagebox.showinfo("Warning", "All fields are required!")
        return
    
    data=load_password()

    if website in load_password():
        ok=messagebox.askyesno("Confirm", "Website already exists. Overwrite?")
        if not ok:
            return

    
    data[website]= {   
        "username": username,
        "password": password   
    }

    with open(FILE_NAME, "w")as file:
        json.dump(data, file, indent=4)

    messagebox.showinfo("Saved", "Password saved successfully!")

    # clear fields after saving
    website_entry.delete(0, END)
    username_entry.delete(0, END)
    pw_entry.delete(0, END)

def find_password():
    website=website_entry.get()
    data=load_password()

    if website in data:
        username=data[website]["username"]
        password=data[website]["password"]

        username_entry.delete(0, END)
        username_entry.insert(0, username)

        pw_entry.delete(0, END)
        pw_entry.insert(0, password)
    else:
        messagebox.showinfo("Error", "No data found for this website!")
        
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

# GUI
root=Tk()
root.title('Strong password generator')
icon_path = os.path.join(os.path.dirname(__file__), "icon.png")
img = ImageTk.PhotoImage(file=icon_path)
root.iconphoto(False, img)
root.geometry("500x500")

# website 
website_entry=Entry(root, font=("Helvetica", 24))
website_entry.insert(0, "Website")
website_entry.pack(pady=5)

# username
username_entry=Entry(root, font=("Helvetica", 18))
username_entry.insert(0, "Username/Email")
username_entry.pack(pady=5)

# Label Frame
lf=LabelFrame(root,text="How many characters")
lf.pack(pady=20)

# create entry box to Designate the number of characters
my_entry=Entry(lf,font=("Helvetica",24))
my_entry.pack(pady=20,padx=20)


# Entry box for our returned passsword
pw_entry=Entry(root, font=("Helvetica",24))
pw_entry.insert(0, "Password")
pw_entry.pack(pady=20)

#create a frame for our buttons
my_frame=Frame(root)
my_frame.pack()

# crate our buttons
my_button=Button(my_frame,text="Generator Strong Password",command=new_rand)
my_button.grid(row=0,column=0,padx=10)
 
clip_button=Button(my_frame,text="Copy to Clipboard",command=clipper)
clip_button.grid(row=0,column=1,padx=10)

save_button=Button(root, text="Save Password", command=save_password)
save_button.pack(pady=5)

search_button=Button(root, text="Search Password", command=find_password)
search_button.pack(pady=5)

root.mainloop()