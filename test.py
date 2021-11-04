import constant as con

def menu():
  print("HELLO!! WELCOME TO {}".format(con.game_name))
  print("here are yor choices = {}".format(con.main_menu_choice))
  user=input('>>>  ').lower().strip()
  while user not in con.main_menu_choices:
    print('sorry unable to recoganize that {}'.format(con.main_menu_choice))
    user=input('>>>  ').lower().strip()

print('your input: {}'.format(user))
if user == 'quit':
  exit() 	

if __name__=='__main__':
	check=True
	while check:
		check=menu()