# Tuples
# ===================================
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(numbers)

# Indexing
numbers[0]

# Lenght 
len(numbers)

# Slicing
#numbers[start: end: step]
print(numbers[0:5:1])
numbers[:5:]
numbers[:5]
numbers[1:8:3]
# Slincng with Negative Indices
print(numbers[-5:])
print(numbers[:-5])

# Adding New Values To a Tuple
a = (1, 2, 3)
b = ('four', 'five', 'ten')
c = a + b
print(c)

# max()
print(max(numbers))

# min()
print(min(numbers))

# count(): Returns the occurrence of any specified value or object in it.
print(numbers.count(3))

# Repetition: generate repeated sequences of a tuple simply by using the 
# asterisk operator * with the number of times
print(numbers * 3)

# in Keyword
print(9 in numbers)
print(10 in numbers)

# The index() function
print(numbers.index(9))
#print(numbers.index(10))

# Modifying Elements in a List
listA = [0, 'one', 'two', 'three', 4, 'five', 6, 'seven']


# Lists
# ======================

# Adding New Elements Into a List

# Append
lnumbers = [0, 'one', 'two', 'three', 4, 'five', 6, 'seven']
lnumbers.append('egith')
print(lnumbers)

# Extend
extras = [9, 'ten', 11]
lnumbers.extend(extras)
print(lnumbers)

# Using the '+' instead of extend()

new_list = [1, 2, 3] + [4, 5, 6]
print(new_list)

# insert
new_list.insert(0, 0)
print(new_list)

# Deleting Elements from a List
# remove(): Removes the leftmost occurrence of that value
lst = [4, 3, 2, 1, 4]
lst.remove(4)         # Value "4" gets removed
print(lst)

# pop(): Deletes the element at a specified position, and returns the deleted element.
#  If no position is specified, it “pops” the last element in the list
lst = [10, 20, 30, 40, 50]
lst.pop(1)
# 20
print(lst)
# [10, 30, 40, 50]

lst.pop()   # No position is specified here
# 50
print(lst)
# [10, 30, 40]

# clear: Clear the entire list
lst.clear()
print(lst)
# []

# Alising
# if you have list a and assign it the name b, the original list a will still exist.
# b acts as an “alias” for the original list, pointing to the same location in the 
# memory where the original list is stored. This means that when you make changes in b,
# they’ll be made in a as well.

a = [10, 20, 30, 40, 50]
b = a
b[2] = 300
print(a)
# [10, 20, 300, 40, 50]

#copy(): To make changes to a copy of your list without affecting the original,
#  you need to use the copy() function.

a = [10, 20, 30, 40, 50]
b = a.copy()
b[2] = 300
print(a)
#[10, 20, 30, 40, 50]    # The original list is unaffected

# Sorting
a = [5, 2, 4, 1, 6, 5, 9, 1]
a.sort()
print(a)
# [1, 1, 2, 4, 5, 5, 6, 9]
a.sort(reverse=True)
print(a)
# [9, 6, 5, 5, 4, 2, 1, 1]

# reverse()
a = [2, 4, 6, 8, 1, 3, 5, 7]
a.reverse()
print(a)
#[7, 5, 3, 1, 8, 6, 4, 2]

# Strings
# ==========================

s_1 = "This is a fruit."
s_2 = 'Fruits are delicious.'

# Concatenation
s1 = 'water'
s2 = 'melon'
print(s1 + s2)
# watermelon

# Strings can also be joined together with custom filler characters (e.g., commas)
# in-between using the join() method, with the following syntax:

# "<filler characters>".join([string 1, string 2, string 3, …])
s1 = "apple"
s2 = "banana"
s3 = "cherries"
all_fruits = ", ".join([s1, s2, s3])
print(all_fruits)
# apple, banana, cherries

s1 = "hello"
s2 = "WORLD"
print(s1.upper())
# HELLO
print(s2.lower())
# world
print(s1.capitalize())
# Hello