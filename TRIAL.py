'''# importing only those functions which 
# are need
  
# time function used to calculate time 
import tkinter as tk
import time
  
# creating tkinter window 
root = Tk() 
  
button = Button(root, text = '9988') 
button.pack(side = TOP, pady = 5) 
  
print('BE VERY VIGILENT....EYES WIDE OPEN...') 
# Calculating starting time 
start = time() 
  
# in after method 5000 miliseconds 
# is passed i.e after 5 seconds 
# main window i.e root window will 
# get destroyed 
root.after(5000, root.destroy) 
  
mainloop() 
  # calculating end time 
end = time()

#label = tk.Label(text="Hello, Tkinter",fg="white",bg="black",width=10,height=10)
#label = tk.Label(text="Hello, Tkinter",fg="white",bg="black",width=10,height=10)

window=tk.Tk()
greeting = tk.Label(text="9988")
greeting.pack()

time.sleep(3)

print('HOPEFULLY YOU GOT THAT AS IT WILL NOT SHOW AGAIN')'''
import tkinter
import time
window = tkinter.Tk()
window.after(10000, lambda: window.destroy())
label1=tkinter.Label(window,text="9988").pack()
button1=tkinter.Button(window,text='CLOSE',command=window.destroy).pack()
time.sleep(2)
window.mainloop()

