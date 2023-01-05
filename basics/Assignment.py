# Driver Application

First_Name = 'Deepak'
Last_Name = 'Shankar'
Age = 33
SSN = 'AAA591234567'
Height = 178
Weight = 81.5
print(First_Name,Last_Name ,Age ,SSN ,Height ,Weight)

# Data Types

num = 10
dec = 20.54
bol = True
str = "I am the best"
print(num)
print(type(num))
print(dec)
print(type(dec))
print(bol)
print(type(bol))
print(str)
print(type(str))

# Collection Types

print("---List of Contries---",'\n')
lst_Cnty=['America','India','UK']
print(lst_Cnty,'\n')

print("---Adding Country at End---",'\n')

lst_Cnty.append('Ukraine')
print(lst_Cnty,'\n')

print("---Removing Country By Index---",'\n')

del (lst_Cnty[0])
print(lst_Cnty)

print("---Adding Country In Middle---",'\n')

lst_Cnty.insert(1,'Japan')
print(lst_Cnty)