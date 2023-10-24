fruits = []

print("Fruits:")
fruits.append("Apple")
fruits.append("Grapes")
fruits.append("Mango")
print(fruits)

drinks = []

print("Drinks: ")
drinks.append("Coffee")
drinks.append("Milktea")
drinks.append("Water")
print(drinks)

print("Enter e to eat a fruit")
eat = input();
if str.lower(eat) == "e":
    print("You ate ", fruits.pop())
    print("Fruits left: ", fruits)
    
eat = input();
if str.lower(eat) == "e":
    print("You ate ", fruits.pop())
    print("Fruits left: ", fruits)

eat = input();
if str.lower(eat) == "e":
    print("You ate ", fruits.pop())
    print("Fruits left: ", fruits)
    
if not fruits:
    print("No more fruits left")


print("Press d to drink a beverage"):
drink = input();
if str.lower(drink) == "d":
    print("You ate ", drinks.pop())
    print("Fruits left: ", drinks)
    
drink = input();
if str.lower(drink) == "d":
    print("You ate ", drinks.pop())
    print("Fruits left: ", drinks)

drink = input();
if str.lower(drink) == "d":
    print("You ate ", drinks.pop())
    print("Fruits left: ", drinks)
    
if not drinks:
    print("No more drinks left")
    

    
