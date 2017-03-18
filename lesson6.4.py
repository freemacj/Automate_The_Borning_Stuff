spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam)) # we have to convert spam to a string in order to concatenate with the string, 'spam is'

# when we run this code note that "spam is 3" is never printed?
# that's because on line 4 we say if spam == 3: then continue
# the continue statement jumps back to the start of the while loop, thus skipping line 6 when spam == 3