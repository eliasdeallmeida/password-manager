def show_menu():
  menu = (
    'Show passwords',
    'Generate password',
    'Update password',
    'Delete password',
    'Exit'
  )
  print(f'{" MENU ":=^35}')
  for count, option in enumerate(menu):
    print(f'{count + 1:.<5}{option:.>30}')


def show_password_menu(selected_options):
  menu = (
    'Lowercase characters',
    'Uppercase characters',
    'Special characters',
    'Numbers',
    'All characters',
    'Clear',
    'Previous',
    'Next'
  )
  print(f'{" PASSWORD MENU ":=^35}')
  for count, option in enumerate(menu):
    if str(count + 1) in selected_options:
      print('[X] ', end = '')
    elif count < 5:
      print('[ ] ', end = '')
    else:
      print('    ', end = '')
    print(f'{count + 1}{option:.>30}')


def show_database(key = False):
  with open('passwords.txt', 'r') as file:
    database = file.readlines()
  print(f'{" PASSWORDS ":=^35}')
  for id, line in enumerate(database):
    line = line.replace('\n', '')
    print(f'{id + 1:.<5}{" " + line:.>30}')
  print()
  if key is True:
    return database
  input('Press ENTER to continue...')

