''' - original broken code
def div42by(divideBy):
    return 42 / divideBy

print(div42by(2))
print(div42by(12))
print(div42by(0)) # notice when our code gets to this line the program will stop running and we receive an error! "ZeroDivisionError: division by zero"
print(div42by(1))
'''

# now we will put together an example where our program will continue even if an error is found

def div21by(divideBy):
    try:
        return 21 / divideBy
    except ZeroDivisionError:
        print('Error: You tried to divide by zero.')

print(div21by(3))
print(div21by(7))
print(div21by(0))
print(div21by(1))