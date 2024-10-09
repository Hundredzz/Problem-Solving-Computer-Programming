"""code"""
def f(lst):
    """function"""
    newlst = lst.split()
    return int(newlst[0]) + int(newlst[1])
def y(lst):
    """function"""
    newlst = lst.split()
    return int(newlst[1])
def main():
    """function"""
    lst = []
    for _ in range(int(input())):
        for _ in range(int(input())):
            lst.append(input())
        lst.sort(key=y, reverse=True)
        lst.sort(key=f)
        for i in lst:
            print(i)
        lst.clear()
main()
