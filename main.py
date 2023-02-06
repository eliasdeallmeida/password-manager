from features import *
from input import *
from output import *

all_characters = (
  'abcdefghijklmnopqrstuvwxyz',
  'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
  '._-@#*',
  '0123456789'
)

while True:
  clear_console()
  show_menu()
  option = input_int('\nYour choice: ')

  if option == 1:
    clear_console()
    show_database()

  elif option == 2:
    option = get_password_option()
    if option is False:
      continue
    generate(all_characters, option)
    
  elif option == 3:
    clear_console()
    database = show_database(True)
    id = input_int('Enter the password ID (0 to go back): ')
    if id == 0:
      continue
    id -= 1
    option = get_password_option()
    if option is False:
      continue
    generate(all_characters, option, id, True)    
  
  elif option == 4:
    clear_console()
    database = show_database(True)
    delete = input_int('Enter the password ID (0 to go back): ')
    if delete == 0:
      continue
    delete -= 1
    database.pop(delete)
    with open('passwords.txt', 'w') as file:
      for line in database:
        file.write(line)

  elif option == 5:
    clear_console()
    break

  else:
    print('>>> ERROR: Enter a valid option', end = '')
    for c in range(3):
      print('.', end = '', flush = True)
      sleep(1)

print('Program was finished.')

