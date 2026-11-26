prices = [450, 1200, 300, 980, 75]
highest = 0
lowest = prices[0]
for i in prices:
    if i > highest :
        highest = i
    if i < lowest:
        lowest = i
print("highest", highest)
print("lowest", lowest)
