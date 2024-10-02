"""code"""
def main():
    """function"""
    num = (int(input()), int(input()))
    maxi = max(num)
    mini = min (num)
    count = 1
    try:
        while True:
            num = mini / count
            if num == 1:
                print("YES\n1")
                break
            if not num:
                print("NO")
                print(maxi)
                break
            if not maxi % num and not mini % num:
                print("NO")
                print(int(num))
                break
            count += 1
    except TimeoutError:
        print("YES\n1")
main()
