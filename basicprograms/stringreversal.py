''' s = input('Enter a string')
print(s[::-1]) 
s = input('Enter a string')
i = len(s)-1
result = ''
while i >= 0:
    result = result+s[i]
    i = i-1
print(result) '''

# s = '-'.join(['a','b','c'])
# print(s)

s = input('Enter a String:')
print(''.join(reversed(s)))