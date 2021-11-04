from tkinter import *
from tkinter import *
tk=Tk()
load = Progressbar(tk,orient=HORIZONTAL,length=1000,mode='determinate')
def bar():
    import time

    load['value']=20
    tk.update_idletasks()
    time.sleep(1)
    load['value']=50
    tk.update_idletasks()
    time.sleep(1)
    load['value']=100
    tk.update_idletasks()
    time.sleep(1)
    load['value']=150
    tk.update_idletasks()
    time.sleep(1)
    load['value']=170
    tk.update_idletasks()
    time.sleep(1)
    load['value']=200
    tk.update_idletasks()
    time.sleep(1)
load.pack()
button(tk,text='start',command=bar).bar()
mainloop()
    
