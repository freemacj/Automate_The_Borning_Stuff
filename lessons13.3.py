# use len() to define the length of a list
apple = len(['bat', 'cat', 'hat', 'zebra'])
print(apple)


# the list() function
banana = list('Hello')
print(banana)


# the `in` operator
pear = 'howdy' in ['hello', 'hi', 'good day', 'howdy', 'goodbye']
print(pear) # howdy is in the list, thus this will be a true statement


# same list, but with the `not in` operator
peach = 'howdy' not in ['hello', 'hi', 'good day', 'howdy', 'goodbye']
print(peach) # howdy is in the list, thus this is a false statement