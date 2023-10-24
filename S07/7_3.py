from mylib import *

command=''
while command not in ['end', 'exit', 'payan', '0']:
    command = textinput("Command", "Enter command: ")
    if command in ['circle', 'dayreh']:
        r = numinput("Radius", "Enter radius")
        circle(r)
    elif command in ['color', 'rang']:
        c = textinput("Color", "Enter color:")
        color(c)
    elif command in ['square', 'moraba']:
        s = numinput("Size", "Enter size:")
        square(s)
    elif command in ['rectangle', 'mostatil']:
        a = numinput("Size", "Enter Width:")
        b = numinput("Size", "Enter Height:")
        rectangle(a, b)
        
