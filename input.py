def input_int(message = 'Enter a integer number: '):
  while True:
    try:
      number = int(input(message))
    except:
      print('>>> ERROR: Enter a valid integer number.')
    else:
      return number

