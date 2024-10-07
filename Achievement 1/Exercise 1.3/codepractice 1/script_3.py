print('\n\nEnter the first number, second number and the operator symbol: \n')
a = int(input('first number: '))
b = int(input('second numner: '))
operator = str(input('Enter the operator symbol \'+\' or \'-\': '))

if operator == '+':
  print('You choose to sum the numbers.')
  print('The sum of the numbers is: ', str(a + b), '\n')
elif operator == '-':
  print('You chose to subtract the numbers.')
  print('The rest of the numbers: ', a - b, '\n')
