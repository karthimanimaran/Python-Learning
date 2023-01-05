### 1.) Maximum of two numbers in Python ###
a=5
b=8
print('*** 1.Maximum of two numbers ***','\n')
if a > b:
    print (a,'\n')
elif b > a:
    print (b,'\n')
else:
    print ('No Results','\n')

### 2.) Find Sum of List ###

print('*** 2.Sum of the List ***','\n')
n = [1,2,3,4,5]
print("Sum of the given numbers is :",sum(n),'\n')

### 3.) Find Largest Number in the List ###

print('*** 3.Largest Number in the List ***','\n')
n = [1,2,3,4,5,6,7,8,9,10]
print("Largest Number in the given list is :",max(n),'\n')

### 4.) Interchange 1st and Last Element in the List ###

print('*** 4.Interchange Elements in the List ***','\n')
lst = [1,2,3,4,5,6,7,8,9,10]
i = len(lst)

temp = lst[0]
lst[0] = lst[i-1]
lst[i-1] = temp
print("Reversed List is :", lst,'\n')

### 5.) Extract Unique dictionary values ###

print('*** 5.Extract Unique Dictionary Values ***','\n')

dict = {'gfg': [5, 6, 7, 8],'is': [10, 11, 7, 5],'best': [6, 12, 10, 8],'for': [1, 2, 5]}

print ("The original dictionary is :",dict,'\n')

uni = []

for i in dict:
    for n in dict[i]:
        if n not in uni:
            uni.append(n)
print("The unique values list is :",sorted(uni),'\n')

### 6.) Ways to remove a key from dictionary ###

print('*** 6.Remove a key from Dictionary ***','\n')

dict = {'Anuradha': 21, 'Haritha': 21, 'Arushi': 22, 'Mani': 21}

print ('Before remove key:',dict,'\n')

del dict['Mani']

print ('After removing key:',dict,'\n')

### 7.) Find the sum of all items in a dictionary ###

print('*** 7.Sum of all items in a Dictionary ***','\n')

dict = {'a': 100, 'b':200, 'c':300}

v = dict.values()

print(sum(v))






