from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('my coding')
root.iconbitmap('C:/Users/josep/Desktop/coding/document.ico')
root.geometry('400x530')

my_img1 = ImageTk.PhotoImage(Image.open('C:/Users/josep/Desktop/coding/images/stick_man.jpg')) 
my_img2 = ImageTk.PhotoImage(Image.open('C:/Users/josep/Desktop/coding/images/stick_man2.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('C:/Users/josep/Desktop/coding/images/stick_man3.jpg')) 
my_img4 = ImageTk.PhotoImage(Image.open('C:/Users/josep/Desktop/coding/images/stick_man4.jpg'))
my_img5 = ImageTk.PhotoImage(Image.open('C:/Users/josep/Desktop/coding/images/stick_man5.jpg')) 


image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]




my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)
status = Label(root, text='1 of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=CENTER)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button (root, text='->', padx=3, pady=3, command = lambda: forward(image_number+1))
    button_back = Button (root, text='<-', padx=3, pady=3, command = lambda: back(image_number-1))

    if image_number == 5:
        button_forward = Button(root, text='->', padx=3, pady=3, state=DISABLED)

    status = Label(root, text=str(image_number)+ ' of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=CENTER)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.place(x=215, y=475)
    button_back.place(x=150, y=475)
    status.place(x=0, y=510, width=400)

def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button (root, text='->', padx=3, pady=3, command = lambda: forward(image_number+1))
    button_back = Button (root, text='<-', padx=3, pady=3, command = lambda: back(image_number-1))
    status = Label(root, text=str(image_number) + ' of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=CENTER)

    if image_number == 1:
        button_back = Button(root, text='<-', state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.place(x=215, y=475)
    button_back.place(x=150, y=475)
    status.place(x=0, y=510, width=400)


button_back = Button(root, text='<-', padx=3, pady=3, command=lambda: back(1))
button_quit = Button(root, text='Exit', padx=3, pady=3, command=root.quit)
button_forward = Button(root, text='->', padx=3, pady=3, command=lambda: forward(2))

button_back.place(x=150, y=475)
button_quit.place(x=180, y=475)
button_forward.place(x=215, y=475)
status.place(x=0, y=510, width=400)

root.mainloop()
