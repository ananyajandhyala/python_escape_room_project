from tkinter import *      
root = Tk()
#canvas = Canvas(width = 450, height = 250,bg='blue')      
#canvas.pack()      
img = PhotoImage(file="D:\\win.png")
label=Label(root,image=img)
label.pack()
#canvas.create_image(0,0, anchor=NW, image=img)      
root.mainloop() 
