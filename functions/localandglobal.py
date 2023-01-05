x = 123

def display():
    #y = 678
    #print(y)
    x = 678
    print(x)
    print(globals()['x'])

print(x)
z = display
z()