"""code"""
def main():
    """function"""
    money = int(input())
    child = int(input())
    money -= child
    if child * 7 < money:
        money = child - 1
    elif money % 7 == 3 and money // 7 == child-1:
        money = (money // 7) - 1
    else:
        money = money // 7
    if money > child:
        print(child-1)
    elif money >= 0:
        print(money)
    else:
        print(-1)
main()
