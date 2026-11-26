products = [("Laptop", 150000, 3), ("Mouse", 2500, 0),
("Keyboard", 5000, 12), ("Monitor", 45000, 2)]
total = 0
for name, price, quantity in products:
    if quantity == 0:
        print("Out of stock:" , name)
    elif quantity >= 1 and quantity <= 4:
        print("Low stock:" , name)
    total += price * quantity
print("Total stock value:" , total)