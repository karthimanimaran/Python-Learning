
lst=[10,20,'Karthi',-10,30.5]
print(lst)
print(lst[3])
print(lst[3:5])
print(lst*4)
print(len(lst))

lst.append(40)
lst.remove('Karthi')
del(lst[1])
print(lst)

# lst.clear()
# print(lst)

print(max(lst))
print(min(lst))

lst.insert(3, 99)
print(lst)

lst.sort(reverse=True)
print(lst) 


"""
n = int(input("Enter Input Number:"))
arr = list(set(map(int, input("Enter the values:").split())))
arr.remove (max(arr))
print(max(arr))
    
"""
"""
N = int(input("Enter the Input:"))
lst = []
    
for i in range(N):
        s=input().split()
        if s[0]=="insert":
            lst.insert(int(s[1]),int(s[2]))
        elif s[0]=="remove":
            lst.remove(int(s[1]))
        elif s[0]=="append":
            lst.append(int(s[1]))
        elif s[0]=="sort":
            lst.sort()
        elif s[0]=="pop":
            lst.pop()
        elif s[0]=="reverse":
            lst.reverse()
        elif s[0]=="print":
            print(lst)
"""