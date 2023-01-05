#### Assignment Using Loops ####

n = int(input('Enter the number :'))
nub = {}
for i in range (n):
    if i % 10 == 0:
        continue
    if i > 100:
        break
    print(i)