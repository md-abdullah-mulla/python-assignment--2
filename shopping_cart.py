name = input("Customer Name: ")

item1 = input("Product 1: ")
price1 = float(input("Price: "))

item2 = input("Product 2: ")
price2 = float(input("Price: "))

item3 = input("Product 3: ")
price3 = float(input("Price: "))

sub = price1 + price2 + price3

if sub >= 5000:
    disc_rate = 0.20
elif sub >= 3000:
    disc_rate = 0.10
elif sub >= 1000:
    disc_rate = 0.05
else:
    disc_rate = 0.00

disc = sub * disc_rate
final = sub - disc

print(f"Customer Name: {name}")
print(f"Product 1: {item1} - Price: {price1:.0f}")
print(f"Product 2: {item2} - Price: {price2:.0f}")
print(f"Product 3: {item3} - Price: {price3:.0f}")
print(f"Subtotal: {sub:.0f}")
print(f"Discount: {disc:.0f}")
print(f"Final Total: {final:.0f}")