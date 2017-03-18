name = ''
while name != 'your name': # we know this is true to start, because we just set name = '' or blank
    print('Please type your name.')
    name = input() # sets name = to the user input. At this point it jumps backs to line 2 to recheck the condition, if input != 'your name' you enter the loop again
print('Thank you')