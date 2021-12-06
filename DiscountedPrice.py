price = input("Enter the price: ")

print("The initial price is: " + price)
price = int(price)

if price > 300:
    price = price - (30/100*price)
elif price >= 200 & price < 300:
    price = price - (20/100*price)
elif price >= 100 & price < 200:
    price = price - (10/100*price)
elif price < 100:
    price = price - (5/100*price)
elif price < 0:
    price = price

print(f"The new price is: {price}")
