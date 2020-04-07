from tkinter import *
from PIL import ImageTk,Image #to get images we use this module

root = Tk()
root.title('Image Viewer')
root.iconbitmap('images/icon.png')
root.geometry("400x350") # to resize the window bar 

my_img1 = ImageTk.PhotoImage(Image.open("images/js.png")) # to insert picture
my_img2 = ImageTk.PhotoImage(Image.open("images/orange.jfif"))
my_img3 = ImageTk.PhotoImage(Image.open("images/cat1.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/bike.jpg"))

image_list = [my_img1,my_img2,my_img3, my_img4] # to set all images in a list

#Creating a status bar 

status = Label(root, text="Image 1 of " + str(len(image_list)),bd=1,relief=SUNKEN,anchor=E) #Anchors are used to define where text is positioned relative to a reference point.


my_label = Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image = image_list[image_number-1])
    button_forward = Button(root,text=">>",command=lambda:forward(image_number + 1 ))
    button_back = Button(root,text="<<",command=lambda:forward(image_number - 1 ))

    if image_number == 5:
        button_forward = Button(root, text=">>", state=DISABLED) # here disabled means we cannot use the forward button when image_number is last in this case 4.

    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)

    status = Label(root, text="Image " + str(image_number)  + " of " + str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)


def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image = image_list[image_number-1])
    button_forward = Button(root,text=">>",command=lambda:forward(image_number + 1 )) # +1 cuz when we click the forward button we see the next pic
    button_back = Button(root,text="<<",command=lambda:forward(image_number - 1 ))

    if image_number == 1:
        button_back = Button(root, text="<<",state=DISABLED) # here disabled means we cannot go back button when image_number is 1

    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)

    status = Label(root, text="Image " + str(image_number)  + " of " + str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)
     

button_back = Button(root, text="<<",state=DISABLED)
button_exit = Button(root, text="<EXIT", command = root.quit)
button_forward = Button(root, text=">>",command =lambda:forward(2))


button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2,pady=10)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)  #sticky fun is used to stretch status bar 


root.mainloop()