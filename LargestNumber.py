"""code"""
def main():
    """function"""
    num1 = input()
    num2 = input()
    num3 = input()
    test1 = int(num1 + num2 + num3)
    test2 = int(num1 + num3 + num2)
    test3 = int(num2 + num1 + num3)
    test4 = int(num2 + num3 + num1)
    test5 = int(num3 + num1 + num2)
    test6 = int(num3 + num2 + num1)
    if test1 >= test2 and test1 >= test3 and test1 >= test4 and test1 >= test5 and test1 >= test6:
        print(test1)
    elif test2 >= test1 and test2 >= test3 and test2 >= test4 and test2 >= test5 and test2 >= test6:
        print(test2)
    elif test3 >= test1 and test3 >= test2 and test3 >= test4 and test3 >= test5 and test3 >= test6:
        print(test3)
    elif test4 >= test1 and test4 >= test2 and test4 >= test3 and test4 >= test5 and test4 >= test6:
        print(test4)
    elif test5 >= test1 and test5 >= test2 and test5 >= test3 and test5 >= test4 and test5 >= test6:
        print(test5)
    else:
        print(test6)
main()
