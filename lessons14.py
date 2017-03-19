for i in [5, 6, 7, 8]:
    print(i)

for x in ['bat', 'cat', 'dog', 'zebra']:
    print(x)

print(list(range(4)))

print(list(range(0, 101, 2))) # print a list of the range values from 0 to 100 in step increments of 2



supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('index ' + str(i) + ' in supplies is: ' + supplies[i])


'''Multiple assignments'''
cat = ['fat', 'orange', 'loud']
print(cat)

size, color, disposition = 'skinny', 'black', 'quiet'
print(disposition)


'''Swapping Variables'''
a = 'AAA'
b = 'BBB'
a, b = b, a # this line of code swaps the two variables

print('This is now the variable now assigned to a: '+ a)
print('This is now the variable now assigned to b: '+ b)



'''Augmented Assignment Operators'''
spam = 42
# the traditional way we are taught to add one to spam is: spam = spam + 1
spam += 1

# the full list of Augmented Assignment Operators can be found here: https://automatetheboringstuff.com/chapter4/