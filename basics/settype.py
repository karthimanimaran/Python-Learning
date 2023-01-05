s={10,20,30,"xyz",10,20,30}

s.update([88,99])
print(s)
print(type(s))

## print (s*3)
s.remove(30)
print(s)

f=frozenset(s)
f.remove(20)