spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam.index('howdy')) # we will use spam.index to look up the index value of the list item, 'howdy'


# the append() and insert() List Methods
eggs = ['cat', 'dog', 'bat', 'zebra']
eggs.append('moose') # this will append the string moose to the end of the list
print(eggs)

eggs.insert(1, 'chicken') # this will insert the string chicken into the 1st index, and bump all other list items up 1
print(eggs)



# the remove() List method
bacon =  ['cat', 'bat', 'rat', 'pig', 'dog']
bacon.remove('rat') # this will remove the rat item from the lsit

print(bacon)



# the sort() List Method
ham = [2, 5, 3.14, 16, -7]
ham.sort()
print(ham)

fruit = ['banana', 'apple', 'pear', 'peach', 'Berry']
fruit.sort()
print(fruit)

# reverse sort keyword
fruit.sort(reverse=True)
print(fruit)

''' Notice that 'Berry' appears first in our sorted list? That's because the sort method follows
"ASSCII-betical" order, where uppercase letters appear first
'''

# disreguard ASSCII-betical order
fruit.sort(key=str.lower) # will convert the strings in the list to lowercase for sorting
print(fruit)