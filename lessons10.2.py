def spam():
    global eggs # this global statement tells python, even though I have an assignment statement for eggs inside this function (on line 3), eggs in this function will always refer to the global eggs variable
    eggs = 'Hello'
    print(eggs)

eggs = 42
spam()
print(eggs)
