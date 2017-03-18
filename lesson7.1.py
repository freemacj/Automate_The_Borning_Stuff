print('My name is')
for i in range(5):
    print('Jimmy Five Times ' + str(i))

'''
#1 The first time this is run i is set to zero. after each iteration of this print function i increases by 1 and so on..
'''


# another example
print("My name is")
for i in range(12, 16):
    print('Chris Five Times ' + str(i))

'''
#2 in the second example the for loop starts at 12 and goes up to, but not including 16
'''


# a third example with for loops
print("My name is")
for i in range(0, 10, 2):
    print('Earl Five Times ' + str(i))

'''
# 3 In this third example we list the start value of 0, the up to (but not including) value of 10, and the lastly
the step count of 2. Meaning go in increments of 2
'''


# a final example of for loops
print("My name is")
for i in range(5, -1, -1):
    print('Sebastian Five Times' + str(i))

'''
in this example we will use a negative step argument in order to count backwards from 5, to (but not including) -1.
Also, our starting value 5 is greater than our next value of -1
'''