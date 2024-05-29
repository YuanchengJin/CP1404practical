items = int(input("Number of items: "))
total_price = 0
DISCOUNT = 0.1
for i in range(items):
    price = float(input("Price of item: "))
    total_price  += price
if total_price > 100:
    total_price = total_price - total_price * DISCOUNT
print(f'Total price for 3 items is ${total_price:.2f}')


