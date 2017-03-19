'''Strings are an Immuateable data type, While Lists are Mutable'''
# in order to modify the 'name' string below, we will first have to slice it in order to change 'a' to 'the'
name = ('Abbey a dog')
newName = name[0:6] + 'the' + name[7:]
print(newName)



# The copy.deepcopy() Function
import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(spam) # by creating a copy.deepcopy() of spam we are able to modify the list values for cheese, without effecting the original values from spam
cheese[1] = 42
print(cheese)
print(spam)



# Line Continuation for lists and strings
fruit = ['apple '
         'banana '
         'orange '
         'pear '
         'grape']
print(fruit)

print('Four score and seven ' + \
      'years ago')