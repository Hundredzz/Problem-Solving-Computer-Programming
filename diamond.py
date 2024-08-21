"""diamond"""
def main():
    """create diamond"""
    num = int(input())
    for i in range(num):
        for j in range(num):
            if i == num // 2:
                print("*",end="")
            elif i < num // 2:
                if j in (num//2 -i,num//2 +i):
                    print("*", end="")
                else:
                    print(" ",end="")
            else:
                if j in (i-num//2,num -(i-num//2)-1):
                    print("*", end="")
                else:
                    print(" ",end="")
        print()
main()
