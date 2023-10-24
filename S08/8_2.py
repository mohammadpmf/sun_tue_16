#          -8        -7          -6        -5        -4          -3            -2              -1
#           0         1           2         3         4           5             6               7
foods = ['pizza', 'lazania', 'hambeger', 'soosis', 'kabab', 'jooje kabab', 'fesenjoon', 'pizza peperoni']
print(foods)
# foods.sort() # برای مرتب کردن صعودی اعضای یک لیست
# foods.sort(reverse=True) # برای مرتب کردن نزولی اعضای یک لیست
# foods.reverse() # لیست را برعکس میکند.
food = input("Enter new food: ")
# foods.append(food) # به آخر لیست آیتم مورد نظر را اضافه میکند.
foods.insert(0, food) # به خانه مورد نظر از لیست آیتم را اضافه میکند.
print(foods[4])
