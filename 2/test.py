g = 10

def show():
    a = g+10
    print(a)

def change():
    global g 
    g = 20

def main ():
    show()
    change()
    print(g)

main()

