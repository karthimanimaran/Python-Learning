lst = [10,20,30,40,7,60,70]
min = None
for i in lst:
    if min is None or (min > i):
        min = i
print(min)
