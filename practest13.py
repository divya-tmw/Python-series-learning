#discount calculator

price = float(input("Enter price:"))

if price >= 500:
    discount = price * 20 / 100
elif price >= 2000:
    discount = price * 10 / 100
else:
    discount = 0

final_price = price - discount

print("Discount:",discount)
print("Final Price:",final_price)