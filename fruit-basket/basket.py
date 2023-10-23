# author @sollano_jhaynefe #
basket = []

def removeFruit():
        basket.pop()
        if not basket:
        	print("No more fruits")
        	exit(0)
        else:
        	print(f"Fruit(s) in the basket: {basket}")
        	

print("Catch and eat any of these fruits: (Apple, Orange, Mango, Guava)")
quantity = int(input("How many fruits would you like to catch? "))

print("Choose a fruit to catch. Press A, O, M, or G.")
for i in range(1, quantity + 1):
            selection = input(f"Fruit {i} of {quantity}: ").lower()
            if selection == "a":
                basket.append("apple")
            elif selection == "o":
                basket.append("orange")
            elif selection == "m":
                basket.append("mango")
            elif selection == "g":
                basket.append("guava")
            else:
                print("Invalid")
                i -= 1

print(f"Your basket now has: {basket}")

while True: 
     eat = input("Press E to eat a fruit. ").lower()
     if eat == "e":
                removeFruit()
     else:
        print("Invalid")
