# Make a list of the months in a year, and store it as months_named
months_named = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Augost', 'September', 'October', 'November', 'December' ]
months_numbered = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

months_dic = dict(zip(months_named, months_numbered))

months_named.clear()
months_numbered.clear()

print(months_dic)
months_dic_list = list(months_dic.items())
print(months_dic_list)

months_extracted = list(months_dic.keys())
print(months_extracted)
