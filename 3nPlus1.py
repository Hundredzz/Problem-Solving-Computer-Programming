"""3nPlus1"""
def main():
    """3nPlus1"""
    while True:
        num = int(input())
        if not num:
            break
        count = 1
        while num != 1:
            if num % 2:
                num = num * 3 +1
            else:
                num /= 2
            count += 1
        print(count)
main()
