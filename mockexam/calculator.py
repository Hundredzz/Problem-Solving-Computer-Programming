"""code"""
def main():
    """function"""
    num = int(input())
    if num > 99999:
        print(9 * 2 + (90)*3 + 900 * 4 + 9000*5 + \
90000 * 6 + (num - 99999) * 7)
    elif num > 9999:
        print(9 * 2 + (90)*3 + 900 * 4 + 9000*5 + \
(num- 9999) * 6)
    elif num > 999:
        print(9 * 2 + (90)*3 + 900 * 4 + (num - 999)*5)
    elif num > 99:
        print(9 * 2 + (90)*3 + (num - 99)*4)
    elif num > 9:
        print(9 * 2 + (num-9)*3)
    elif num > 1:
        print(num*2)
    else:
        print(num)
main()
