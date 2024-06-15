with open('number_list.txt', 'w') as my_file:
  numbers = [str(number)+'\n' for number in range(50, 101)]
  my_file.writelines(numbers)
  