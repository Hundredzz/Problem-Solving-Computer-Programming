"""code"""
def up(i):
    """up pattern"""
    for k in range(5):
        if k == 2:
            print("*",end="")
        elif k in (2+i,2-i):
            print("*",end="")
        else:
            print(" ",end="")
def down(i):
    """down pattern"""
    for k in range(5):
        if k == 2:
            print("*",end="")
        elif k in (i-2,i+2,i) and 2<=i <4:
            print("*",end="")
        else:
            print(" ",end="")
def left(i):
    """left pattern"""
    for k in range(5):
        if i == 2:
            print("*",end="")
        elif k in (i-2,2-i):
            print("*",end="")
        else:
            print(" ",end="")
def right(i):
    """right pattern"""
    for k in range(5):
        if i == 2:
            print("*",end="")
        elif k in (i+2, i-2) and i !=3:
            print("*",end="")
        elif i == 3 and k == i:
            print("*",end="")
        else:
            print(" ",end="")
def main():
    """function"""
    text = input()
    for i in range(5):
        for j in text:
            if j == "U":
                up(i)
                print(" ",end="")
            elif j == "D":
                down(i)
                print(" ",end="")
            elif j == "L":
                left(i)
                print(" ",end="")
            elif j == "R":
                right(i)
                print(" ",end="")
        print()
main()
