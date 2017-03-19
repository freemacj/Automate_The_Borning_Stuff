spam = ['cat', 'bat', 'ant', 'elephant']

print(spam)
print(spam[0]) # add the value of zero to pull the first item from the list
print(spam[1])
print(spam[2])
print(spam[3])


# lists can also contain other lists
eggs = [['fish', 'sheep', 'bear'], [32, 76, 85]]

print(eggs[0])
print(eggs[1])
print(eggs[0][2]) # you can add a second selector to choose just one item from one of the lists
print(eggs[1][0])


# say you have a very long list, simply use a negative number to pull the last item from the list, etc.
bacon = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(bacon[-1])
print(bacon[-2]) # second to last item on the bacon list


# you can also use lists with string concatenation
print('I am not yet ' + str(bacon[2]) + ' years old')


# you want two items from your spam list above? use a slice, as indicated below with a :
print(spam[1:3]) # like the range() function, split will go up to but not including item 3 from the spam list