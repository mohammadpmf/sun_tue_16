total = 0
# for i in range(1000):
#     price = int(input("Enter item's price: "))
#     if price == 0:
#         break
#     total = total+price
price = int(input("Enter item's price: "))
while price!=0:
    if price>0:
        total = total+price
    price = int(input("Enter item's price: "))
print(f"Total price is: {total}")

