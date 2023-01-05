print("**** Welcome To MyWay Sandwich ****")
print("Pick Any Three Toppings Given Below :")
print(" 1.Onion\n","2.Lettuce\n","3.Tomato\n","4.Olives\n","5.peppers\n","6.Spices")
Toppings = [int(t) for t in input("Enter the Topping Numbers Seperated by Comma : ").split(',')]
sw = int(input("How many Sandwich Would you like to have : "))
print("Total = $",5*sw)
