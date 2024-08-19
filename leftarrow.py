"""code"""
def main(row,column):
    """function"""
    num = column //2
    for _ in range(column):
        for _ in range(abs(num)):
            print(" ",end="")
        print("*"*row)
        num -= 1
main(int(input()),int(input()))
