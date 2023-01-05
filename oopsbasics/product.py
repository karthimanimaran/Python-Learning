class Product:

    def __init__(self):
        self.name = 'IPhone'
        self.description = 'Its Awesome'
        self.price = 700

#Destructor

    def __del__(self):
        print('Inside the destructor')

# Instance Method

    def display(self):
        print(self.name)
        print(self.price)
        print(self.description)

    
p1 = Product()
p1.display()
p1 = None

# print (p1.name)
# print (p1.description)
# print (p1.price)

p2 = Product()
p2.display()
p2 = None

# print (p2.name)
# print (p2.description)
# print (p2.price)