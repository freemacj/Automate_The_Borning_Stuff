#Global and Local Scopes

spam = 42 # global variable

def eggs():
    spam = 42 # local variable

print('some code here')
print('some more code here')

'''
Each function has it's own local scope

In this example lines 3, 8, & 9 are all global scope, while 8 & 9 are local scope to the eggs function

All variables are either one or the other, a variable cannot be both.

Local scope is created whenever a function is called, and once the function is returned these variables are forgotten.
'''

'''
1. Code in the global scope cannot use any local variables
2. Code in a local scope can access global variables.
3. Code in one function's local scope cannot use variables in another local scope.
4. You can use the same name for different variables if they're in different scopes.
'''