import sys,time,os
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

print(color.BOLD + 'loading...' + color.END)
msg = 'LOADING...'
def typewriter(msg):
    for char in msg:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char !='\n':
            time.sleep(1)
        else:
            time.sleep(1)

os.system('cls')
typewriter(msg)

