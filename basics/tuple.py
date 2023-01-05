"""
tpl = (20,30,40,'xyz')
print (type(tpl))
print (tpl*3) 
print (tpl.count(20))
print (tpl.index('xyz'))

lst=[67,34,"xyz"]
print(type(lst))
tpl1=tuple(lst)
print(type(tpl1))
print(tpl1)

"""

if __name__ == '__main__':
    n = int(input("Enter the Number:"))
    integer_list = map(int, input().split())
    # print(integer_list)
    t=(integer_list)
    print(hash(t))