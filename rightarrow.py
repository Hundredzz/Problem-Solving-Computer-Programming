"""code"""
def main(row,column):
    """function"""
    num = 0
    for i in range(column):
        for _ in range(abs(num)):
            print(" ",end="")
        print("*"*row)
        if i < column //2:
            num += 1
        else:
            num-=1
main(int(input()),int(input()))
