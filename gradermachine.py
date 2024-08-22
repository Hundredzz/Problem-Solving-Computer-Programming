"""code"""
def loop(num,last,step):
    """function"""
    sumnum =0
    for i in range(num,last,step):
        if not i % 2:
            print(i, end=" ")
            sumnum += i
    return sumnum
def main():
    """function"""
    num = int(input())
    last = int(input())
    sumnum = 0
    print("pass : ", end="")
    if num > last:
        sumnum = loop(num,last-1,-1)
    else:
        sumnum = loop(num,last+1,1)
    print()
    print(f"Sum : {sumnum}")
main()
