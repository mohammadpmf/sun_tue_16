import string
mylist = string.ascii_letters+string.digits
92**2
92**3
92**4
92**5
92**6
'a9mohammadM#345M755ddv'
password = 'abc4ef'
for i in mylist:
    for j in mylist:
        for k in mylist:
            for t in mylist:
                for i2 in mylist:
                    for i3 in mylist:
                        guess = i+j+k+t+i2+i3
                        if password == guess:
                            print(f"Password is {guess}")
                            exit()
print("End.")