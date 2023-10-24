prices = {
    'pizza'        : 185000,
    'lazania'      : 125000,
    'hambeger'     : 190000,
    'soosis'       : 200000,
    'kabab'        : 23232,
    'jooje kabab'  : 180000,
    'sibzamini'    : 110000,
}
print(prices)
b = int(input("Enter its price: "))
prices.update({'pizza':b})
# prices[a]=b
print(prices)
# food = input("what do you need?")
# if food in prices:
#     print(f"Price is {prices[food]}")
# print(f"Price is {prices.get(food, 0)}")
