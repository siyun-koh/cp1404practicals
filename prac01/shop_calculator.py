itemTotal = 0
itemNumber = int(input("Enter number of items: "))
while itemNumber < 0:
    print("Invalid number entered!")
    itemNumber = int(input("Enter number of items:"))
for i in range(itemNumber):
    price = float(input("Price of item: "))
    itemTotal += price
if itemTotal > 100:
    itemTotal *= 0.9
print("The total price for your ", itemNumber, " items is $", itemTotal, sep='')

# using string formatting from practical 02:
print("The total price for your {} items is ${:,.2f}".format(itemNumber, itemTotal))