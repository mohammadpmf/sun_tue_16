try:
    f = open('contacts.txt', 'r')
    mylist = f.readlines()
    contacts = {}
    for item in mylist:
        temp = item.strip()
        temp = temp.replace(')', '')
        temp = temp.replace('(', '')
        temp = temp.replace("'", '')
        temp = temp.split(',')
        contacts[temp[0]]=temp[1]
except FileNotFoundError:
    contacts = {}
name = input("Enter name:")
while name!='end':
    if name in contacts:
        print(f"{name}: ----{contacts.get(name)}")
    else:
        print("Not in contacts.")
        a = input("Want to add?").lower()
        if a == 'yes':
            number = input("Enter number: ")
            contacts[name]=number
            # contacts.update({name:number})
    name = input("Enter name:")
f = open('contacts.txt', 'w')
f.write(str(contacts))
print(contacts)
# سه تا تابع دیکشنری ها رو بگم. items keys values
# و کار با فایل ها رو کامل بگم. تفاوت a و w رو نشون بدم. جلسه پیش نشون نداده بودم. فقط گفتم.
# بعدش بازی سنگ کاغذ قیچی رو درست کنم.
# بعدش بازی هنگ من رو بگم و وسط بازی هنگ من، توابع استرینگ ها رو بگم. نشد بذارم جلسه بعد.
