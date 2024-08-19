"""code"""
def main():
    """function"""
    while True:
        num = input()
        if not int(num):
            break
        while True:
            num = list(map(int, num))
            num = sum(num)
            if len(str(num)) == 1:
                print(num)
                break
            num = str(num)
main()
