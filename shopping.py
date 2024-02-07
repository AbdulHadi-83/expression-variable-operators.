budget = int(input("Enter your budget: "))  

shopping_list = {}  

while True:
    item_name = input("Enter item name (or 'done' to finish): ")
    if item_name == "done":
        break
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per unit: "))

    shopping_list[item_name] = {"quantity": quantity, "price": price}

