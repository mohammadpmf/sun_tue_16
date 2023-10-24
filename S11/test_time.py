from time import sleep
wrong = 0
p = input("Enter password: ")
while p!="mohammad":
    wrong = wrong + 1
    print(f"You entered wrong password for {wrong} times!")
    if wrong>3:
        for i in range(wrong, 0, -1):
            print(f"You must wait for {i} seconds to enter next password:")
            sleep(1)
    input("Enter password: ")
print("Welcome.")