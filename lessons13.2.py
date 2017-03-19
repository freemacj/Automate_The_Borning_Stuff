spam = [10, 20, 30]

#rename one of these list items... for example '20'

spam[1] = 'Hello'

print(spam)



#rename multiple items on a list by using a slice
eggs = [12, 24, 17, 13, 26]
eggs[3:5] = ['dog', 'cat'] # using slice replace item 3 up to but not including item 5 with ...

print(eggs)



#use shortcuts with slice as well by only including one of the two numbers
bacon = ['cat', 'bat', 'mouse', 'sheep', 'elephant', 'zebra']

print(bacon[:3]) # starting from the beginning of the list up to but not including index 3

print(bacon[3:]) # starting from index 3 all the way to the end of the list




# delete value from a list use the del function
ham = [10, 20, 30, 40, 50, 60, 70]

del ham[3] # delete item 3 from the list
print(ham)