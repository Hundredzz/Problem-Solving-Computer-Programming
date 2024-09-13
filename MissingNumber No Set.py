"""MissingNumber No Set"""
def main():
    """MissingNumber No Set"""
    n =int(input())
    lst_all = []
    lst = []
    for i in range(1,n+1):
        lst_all.append(i)
    while True:
        x = int(input())
        if not x:
            break
        lst.append(x)
    lst.sort()
    for i in lst_all:
        if not i in lst:
            print(i)
main()
