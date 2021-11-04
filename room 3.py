import random
import time
import sys
import winsound

print('####################################################################################################################################################')
print()
print("ENTERING THE LAST AND FINAL ROOM... OH BOY! YOU ARE NOT READ FOR THIS...")
print()
print('####################################################################################################################################################')
time.sleep(1)
print()
print("YOU NOW FIND YOURSELF IN ROOM 4")
print()
print('####################################################################################################################################################')
print()
time.sleep(1)
print("well well well look who made it so far, i must say, you put up quite the fight till now just one last room to escape and get what you need AKA the document to win battle...")
print("do you have what it takes??????? MUAHAHAHAHA")
ip1=(input("would you like to continue?(yes/y/no/n)>>> ")).lower().strip()
print()
if(ip1=='no' or ip1=='n'):
    print("congratulations for making it this far...but unfortunately you have been declared DEFEATED.You are now answerable to the loss your team holds :(")
    print("BETTER LUCK NEXT TIME!")
    #exit
    sys.exit("you have exited the game.THANK YOU for playing")
elif(ip1=='yes' or ip1=='y'):
    print('the sun starts to set outside reminding you of time crunch better HURRY UP!!\n')
    print('on the rustic china cabinet lies an electronic device\n')
    print('on it is a delicate paper that reads...this gadget holds the code to the key kept in the safe make sure to get the code before it is DESTROYED')
    print("click on the button")
    time.sleep(3)
    print('DISCLAIMER: CLICK ON RED BUTTON WITH ATMOST CAUTION!!!!')
    time.sleep(3)
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 3000  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)
time.sleep(1)
import tkinter
window = tkinter.Tk()
window.after(10000, lambda: window.destroy())
label1=tkinter.Label(window,text="9988").pack()
button1=tkinter.Button(window,text='CLOSE',command=window.destroy).pack()
time.sleep(2)
window.mainloop()
print('HOPEFULLY YOU GOT THAT AS IT WILL NOT SHOW AGAIN!!')
print()
print('use the code accquired to open the safe and get your hands on the key, BE QUICK CLOCKS TICKING...')
s=int(input('enter the code!!!>>> '))
print()
time.sleep(1)
print('...WHOOSHH... a sound comes as you set your eys on the prize the document')
time.sleep(1)
print()
print('CONGRATULATIONS!!!!!! NOW YOR VICTORY IS ASSURED AS LONG AS YOU GET BACK ON TIME...')

print('buckle up only minutes before you help save your organisation')


    
    
          
      
