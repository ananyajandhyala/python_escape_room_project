
import random
import time
import sys
import winsound

game_name = "FORT COLLINS:THE SCANDAL IN BELGRAVIA"
main_menu_choice = ["new","quit"]
max_length_for_name = 20
min_length_for_name= 2

from tkinter import *      
root = Tk()
#create a root in gui and locate file location of picture      
img = PhotoImage(file="D:\\escape3.png")
label=Label(root,image=img)
label.pack()
root.after(7000, lambda: root.destroy())#sets time of 10 seconds
#goes back to mainloop of cui.      
root.mainloop()
print("HELLO!! WELCOME TO {}".format(game_name))
time.sleep(2)
print("here are your choices = {}".format(main_menu_choice))
user=input('>>>  ').lower().strip()
'''while user not in main_menu_choices:
  print('sorry unable to recoganize that {}'.format(main_menu_choice))'''
if user == 'quit':
 #exit
 sys.exit("you have exited the game.THANK YOU!! HOPE TO SEE YOU SOON")#comes out of the game   
user=input('ENTER CHARACTER NAME >>>  ').upper().strip()
enter=user    
print('your input: {}'.format(enter))
'''if user == 'quit':
 exit()'''     	

'''if __name__=='__main__':
	check=True
	while check:
		check=menu()'''
print('INPUT YOUR CHOICE OF CHARACTER(1/2)>>> ')
print('######################################################################################################################################################')
print()

print('                                   1)')




print('                                            &&&&&&&&&&&&&&&&')
print('                                          &&&&&&&&&&&&&&&&&&&&')
print('                                         &&&&&&-----------&&&&&&')
print('                                        &&&&&*             *&&&&&')
print('                                       &&&&&*               *&&&&&')
print('                                      &&&&&*                 *&&&&&')
print('                                     &&&&&&*                 *&&&&&&')
print('                                    &&&&&&&*                 *&&&&&&&')
print('                                            *               * ')
print('                                              *            * ')
print('                                                *--------* ')
print('                                              /$$$$$$$$$$$$\ ')
print('                                           /$$$$$$$$$$$$$$$$$$\ ')
print('                                        /$$$$$$$$$$$$$$$$$$$$$$$$$\ ')
print('                                     /$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\ ')
print('######################################################################################################################################################')

print('                                 2)')
print()

print('                                                _________ ')
print('                                              :           : ')
print('                                            :               : ')
print('                                           :                 : ')
print('                                           :                 :  ')
print('                                           :                 : ')
print('                                            :               : ')
print('                                              :            : ')
print('                                                :________: ')
print('                                             /$$$$$$$$$$$$$$\ ')
print('                                           /$$$$$$$$$$$$$$$$$$\ ')
print('                                        /$$$$$$$$$$$$$$$$$$$$$$$$\ ')
print('                                     /$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\ ')
print('######################################################################################################################################################')
print()

user_in = int(input('enter your choice >>> '))
                       
char = 0
if user_in==1:
  char = 1
elif user_in==2:
  char = 2
                         
def selection(x):
  if x==1:
    print('YOU ARE NOW THE WITTY AND BRAVE FEMALE AGENT')
    print('AGENT {}'.format(enter))
  elif x==2:
    print('YOU ARE NOW THE COURAGEOUS AND QUICK MALE AGENT')
    print('AGENT {}'.format(enter))
if char!=0:
  selection(char)
time.sleep(2)  
print('LET US DIVE INTO THE GAME NOW....')
print()
time.sleep(1)
print('######################################################################################################################################################')
print()
print("""Great! We are now off to start the game, brace yourself. \n 
        THE SETTING:
        You are the member of a secret organisation, you have to infiltrated a highly respected government official's embassy in Belgravia 
        to find a particular document. As a patriot of the opposition, the fate of the battle lies in your hands. To win the battle, find the document""")
time.sleep(1)
ch1=(input("Would you like to continue?(yes/no)>>> ")).lower()
time.sleep(1)
if (ch1=="no"):
        print("you have been defeated in the battle and have let your team down.")
        #exit
        sys.exit("you have exited the game.THANK YOU!! HOPE TO SEE YOU SOON")#comes out of the game  
elif (ch1=="yes"):
        print("""when You break in to the cabin through a window, you are positioned at the west end of the room. 
                next to you is a huge apothecary desk with a small stack of folders on one side, the name plate of the government official's cabin.\n
                There are many other objects that are present on an other government official's desk.
                You also see that the apothecary desk is lined by four drawers on either sides, except that all the drawers do not have knobs. 
                Drawers 1,3,4,6 and 8 do not have knobs. Opposite to the desk is a door, to enter the cabin and there are quite a few paintings\n
                that have been hung up on the walls. On the west side wall there are numerous books mounted on the shelves and there is another door,\n
                you walk towards the door and try to open it but the door is locked and you need a key to open the door.\n
                You look around the room for the key.what do you do?""")
        print('1) Look under the paintings')
        print()
        print('2) Look under the carpets')
        print()
        print('3) Look in the drawers')
        print()
        def choice2():
                global ch2
                ch2=int(input("Enter your choice>>> "))
        choice2()
        def paintings():
                print("You look under the paintings but do not find anything. Wait for a while before you choose again")
                time.sleep(5)
                
                choice2()
                if ch2==2:
                        carpets()
                elif ch2==3:
                        #c=3
                        #print('you now have 2 more chances before time out')
                        #print('you now have 2 more chances before time out',c)
                        
                        drawers()
                        #c+=1
                        #print('you now have 2 more chances before time out')
                        
        def knobs():
                print("""You look at the drawers without the knobs, you need to play smart,and having prior expierence \n
                         the drawers that do not have knobs, are the drawers 1,3,4,6 and 8.""")
                s = int(input('what do you do...you enter the code...>>> '))
                if( s == 13468):
                    pass
                else:
                    #exit
                    sys.exit("you have exited the game.THANK YOU!! HOPE TO SEE YOU SOON")#com
                print(' the safe opens and you find the key to the door that was locked.You then go to the door and insert the key into the keyhole and open the door to ROOM-2')
        def choice3():
                        global ch3
                        ch3=int(input("Enter your choice>>> "))
        def carpets():
                print(""""You look under the carpets and find a small door. You open the door and find a small chest that is password protected.\n
                          How do you find out the password?""")
                print("""1) You look at the drawers without the knobs""")
                print()
                print('2) You look for secret patterns in the arrangement of the books on the shelves')
                choice3()
                if ch3==1:
                        knobs()
                elif ch3==2:
                        books()
        def books():
                print("""You take a close look at the arrangement of the books and do not find any special arrangement
                        Wait for sometime before you get to choose again""")
                time.sleep(5)
                choice3()
                if ch3==1:
                        knobs()
        def drawers():
                print("""You try to open the drawers, you can open only the ones that have knobs, but cannot open the ones without the knobs.\n
                        You do not find anything in the ones you could open.Wait for a while before you choose again.""")
                time.sleep(5)
                choice2()
                if ch2==1:
                        paintings()
                        #c+=1
                        #print('you now have 2 more chances before time out')
                elif ch2==2:
                        carpets()
        if ch2==1:
                paintings()
        elif ch2==2:
                carpets()
        elif ch2==3:
                drawers()
print()
print('######################################################################################################################################################')
print()
from tkinter import *      
root = Tk()
#create a root in gui and locate file location of picture    
img = PhotoImage(file="D:\\room2.png")
label=Label(root,image=img)
label.pack()
root.after(4000, lambda: root.destroy())#sets time of 10 seconds
#goes back to mainloop of cui.
root.mainloop()

print("""Glad that you opened the door! \n
Next your destination is ROOM-2. Go inside and search whether there are any clues about the  document. There you observe two doors.
One is at the south direction and another at the east direction.
Which door do you open?
        \n
        1)EAST direction door
        \n
        2)SOUTH direction door""")
print()
print("""There is Pindrop silence in the room,the ticking of the clock in that room reminds you that time is running out.
Unfortunately the room doors are all locked.""")
Door=int(input("Which room's door will you unlock?(1/2)>>> "))
def Door1():
    if Door==1:
       print("""You are planning to enter the ROOM-3 which is at the east direction.That door is locked by a triangular knob.
           That knob has a keyhole.You are now wondering whether you have to:
           \n
         1)Rotate the knob by 180 degree \n
         2)Search for keys """)
       print()
       Unlock1=int(input("How you are going to unlock the door?(1/2)>>> "))
       if Unlock1==1 :
          print("Turn the knob by 180 degree") 
          print("Locked door knob is in this pattern")  
          def pattern(n):
            k=2*n-2
            for i in range(0,n):
                for j in range(0,k):
                   print(end=" ")
                k=k-1
                for j in range(0,i+1):
                  print("*",end=" ")
                print("\r")
          n=5
          pattern(n)
          print("Unlock the door knob by rotating it") 
          def pattern(n):
             k=2*n-2
             for i in range(n,-1,-1):
                for j in range(k,0,-1):
                   print(end=" ")
                k=k+1
                for j in range(0,i+1):
                  print("*",end=" ")
                print("\r")
          n=4
          pattern(n)
          print('######################################################################################################################################################')
          print()
          print("""Hey, you unlocked the door. After getting inside the ROOM-3, you are going to realise that there is no further room
to navigate for the document.It's a Deadend!! Hurry up, search for the document.""")      
       elif Unlock1==2:
             print ("""You have to search for a key in the room. You find a box that has the symbol of a key, you are open the box eagerly.
But it requires a Current password, to be opened.You start searching for any type of hints around you, you get suspicious about the 
'Current' word that has been shown on the box. You realise that the password changes in a certain period.\n
You notice that there is a digital board which is showing yesterday's, today's as
well as tommorow's date, including the month and the year.
                \n
                1)the present year-the present month-yesterday's date
                \n
                2)the present year-the present month-today's date""")
             print()
             def choice3():
                 global Password
                 Password=int(input("which date you are going to enter as a password?(1/2)>>> "))
             def Password1():
                 print("You are going to enter yesterday's date as password")
                 import datetime
                 today=datetime.date.today()
                 yesterday=today-datetime.timedelta(days=1)
                 print(yesterday)
                 d=int(input('enter the password here >>> '))
                 print(d)
                 print('####################################################################################################################################################')
                 print()
                 print("Oh no!The password you entered is wrong and the box shows a redlight and asks you to 'Try again' after 5 seconds.")
                 time.sleep(5)
                 print("What is the new password that you choose?")
                 choice3()
                 if Password==2:
                     Password2()
             def Password2():
                 print("You are going to enter Today's date as the password")
                 import datetime  
                 today=datetime.date.today()
                 print(today)
                 d1=int(input('enter the password here >>> '))
                 print(d1)
                 print('######################################################################################################################################################')
                 print()
                 print("Password is correct and you see that the box shows a greenlight and it opens. Take the key inside the box and unlock the door to ROOM-3.")
                 print("Start looking for the required document.")
             choice3()
             if Password == 1:
               Password1()
             elif Password == 2:
               Password2()
if Door == 1:
     Door1()
elif Door == 2:
        print('######################################################################################################################################################')
        print()
        import time
        print("You open the door of the room. And enter into ROOM-4")
        print("""You now see that the room is completely empty, except that there is a carving in the wall, you now go near the wall...\n
and see that the engravings are in morse code,
you look around the room and find a small sheet of paper with the morse code and the representation:
A	.-
B	-...
C	-.-.
D	-..
E	.
F	..-.
G	--.
H	....
I	..
J	.---
K	-.-
L	.-..
M	--
N	-.
O	---
P	.--.
Q	--.-
R	.-.
S	...
T	-
U	..-
V	...-
W	.--
X	-..-
Y	-.--
Z	--..
The code engraved on the wall is:
--.  --- / -...  .-  -.-.  -.-
Figure out what the code says!""")
        time.sleep(5)
        print("""What did the code say?
1) Jump out
2) Go back""")
        def choice4():
            global decision
            decision=int(input("Enter your choice>>> "))
        choice4()
        def jump_out():
            print("You jump out the window and fall to your death. You have let your organisation that you strongly believe in down")
            #exit
            sys.exit("you have exited the game.THANK YOU!! HOPE TO SEE YOU SOON")#comes out of the game
        def go_back():
            print('####################################################################################################################################################')
            print()
            time.sleep(2)
            print("You now go back to the ROOM-2, where you can try and open the door at the west end of the room")
            Door1()
        if decision==1:
            jump_out()
        elif decision==2:
            go_back()

  
print()           
print('######################################################################################################################################################')
print()
time.sleep(3)
from tkinter import *      
root = Tk()
#create a root in gui and locate file location of picture    
img = PhotoImage(file="D:\\room3.png")
label=Label(root,image=img)
label.pack()
root.after(4000, lambda: root.destroy())#sets time of 10 seconds
#gos back to mailoop of cui     
root.mainloop()
print("ENTERING THE LAST AND FINAL ROOM... OH BOY! YOU ARE NOT READY FOR THIS...")
print()
print('######################################################################################################################################################')
time.sleep(1)
print()
print("YOU NOW FIND YOURSELF IN ROOM-3")
print()
print('######################################################################################################################################################')
print()
time.sleep(1)
print("well well well look who made it so far, i must say, you put up quite the fight till now just one last room to escape and get what you need...")
print('AKA the document to win battle...')
print("Do you have what it takes??????? MUAHAHAHAHA")
ip1=(input("would you like to continue?(yes/y/no/n)>>> ")).lower().strip()
print()
if(ip1=='no' or ip1=='n'):
    print("Congratulations for making it this far...but unfortunately you have been declared DEFEATED.You are now answerable to the loss your team holds :(")
    print("BETTER LUCK NEXT TIME!")
    #exit
    sys.exit("You have exited the game.THANK YOU!! HOPE TO SEE YOU SOON")#comes out of the game
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
window.after(7000, lambda: window.destroy())#sets time of 10 seconds
label1=tkinter.Label(window,text="9988").pack()
button1=tkinter.Button(window,text='CLOSE',command=window.destroy).pack()
time.sleep(2)
window.mainloop()
print('HOPEFULLY YOU GOT THAT AS IT WILL NOT BE SHOWN AGAIN!!')
print()
print('Use the code accquired to open the safe and get your hands on the key, BE QUICK CLOCKS TICKING...')
s=int(input('Enter the code!!!>>> '))
if s==9988:
 print()
 time.sleep(1)
 print('####################################################################################################################################################')
 print()
 print('...WHOOSHH... A sound comes as you set your eyes on the prize.... THE DOCUMENT')
 time.sleep(1)
 from tkinter import *      
 root = Tk()
 #create a root in gui and locate file location of picture      
 img = PhotoImage(file="D:\\docpic.png")
 label=Label(root,image=img)
 label.pack()
 root.after(4000, lambda: root.destroy())#sets time of 10 seconds
 #goes back to mainloop     
 root.mainloop() 
 
 print()
 print('####################################################################################################################################################')
 print()
 print('CONGRATULATIONS!!!!!! WELL DONE AGENT{}. NOW YOUR VICTORY IS ASSURED AS LONG AS YOU GET BACK ON TIME...'.format(user))
 time.sleep(1)
 from tkinter import *      
 root = Tk()
 #create a root in gui and locate file location of picture      
 img = PhotoImage(file="D:\\win.png")
 label=Label(root,image=img)
 label.pack()
 root.after(4000, lambda: root.destroy())#sets time of 10 seconds
 #goes back to mainloop      
 root.mainloop()
 
 print('Buckle up only minutes before you help save your organisation')
 print('####################################################################################################################################################')
 print()
else:
    print('You failed to enter the right code AGENT {}. YOU WILL NOW FACE ITS CONSEQUENCES >>> '.format(user))
    #exit
    sys.exit("You have exited the game.THANK YOU!! HOPE TO SEE YOU SOON AGENT {}".format(user))#comes out of the game
 
