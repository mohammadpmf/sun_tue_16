import json
try:
    f = open('contacts.json', 'r')
    contacts = json.load(f)
    f.close()
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
f = open('contacts.json', 'w')
json.dump(contacts, f, indent=4)
f.close()
print(contacts)