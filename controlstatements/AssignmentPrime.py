n = int(input("Enter a Number:"))
primeflag = False

if n > 1:
    for i in range (2,n):
        if (n%i) == 0:
            primeflag = True
            break
if primeflag:
    print(n,'is not a prime number')

else:
    print(n,'is a prime number')


