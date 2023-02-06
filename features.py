from os import system, name
from random import choice
from time import sleep

from input import input_int
from output import show_password_menu


def clear_console():
  system('cls' if name == 'nt' else 'clear')


def read_database(key = False):
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


def get_password_option():
  selected_option = ''
  while True:
    clear_console()
    show_password_menu(selected_option)
    option = input_int('\nYour choice: ')
    if 1 <= option <= 4:
      selected_option += str(option)
    elif option == 5:
      selected_option = '12345'
    elif option == 6:
      selected_option = ''
    elif option == 7:
      return False
    elif option == 8:
      if selected_option == '':
        print('>>> ERROR: You didn\'t selected any password option')
        input('Press ENTER to continue...')
        continue
      break
    else:
      print('>>> ERROR: Enter a valid option', end = '')
      for c in range(3):
        print('.', end = '', flush = True)
        sleep(1)
  return selected_option.replace('5', '')


def generate(all_characters, option, id = False, key = False):
    clear_console()
    password_length = get_password_length()
    characters = set_valid_characters(all_characters, option)
    password = generate_password(characters, password_length)
    print(f'Password generated: {password}')
    save = confirm('Do you want to save the password? [Y/N] ')
    if save is True:
      if key is True:
        with open('passwords.txt', 'r') as file:
          database = file.readlines()
          database[id] = password + '\n'
        with open('passwords.txt', 'w') as file:
          for line in database:
            file.write(line)
      else:
        with open('passwords.txt', 'a') as file:
          file.write(password + '\n')
        print('\nPassword was saved successfully.')
    else:
      print('\nPassword was not saved.')
    input('Press ENTER to continue...')


def get_password_length():
  while True:
    length = input_int('Enter the password length: ')
    if 8 <= length <= 16:
      clear_console()
      return length
    print('>>> ERROR: The password length should be between 8 and 16.\n')


def set_valid_characters(all_characters, option):
  characters = ''
  for op in option:
    characters += all_characters[int(op) - 1]
  return characters


def generate_password(characters, length):
  return ''.join(choice(characters) for c in range(length))


def confirm(message = '\nDo you want to continue? [Y/N] '):
  while True:
    answer = str(input(message)).strip().upper()[0]
    if answer == 'Y':
      return True
    elif answer == 'N':
      return False
    print('>>> ERROR: Enter Y for Yes or N for No.')

