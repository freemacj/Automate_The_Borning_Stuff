name = ''
while True: # using will true will run indefinitely
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break # called a break statement, essentially breaking you out of the loop
print('Thank you')

# using this method we will never break out of the 'while true' loop because the statement will never be false
# instead we've set this so that, if name == 'your name': we will 'break' the loop, thus printing thank you