print('How many dogs do you have?')

numDogs = input()

try:
    if int(numDogs) >= 4:
        print('That\'s a log of dogs!')
    else:
        print('That\'s not that many dogs...')
except ValueError:
    print('Please enter numeric values only')
