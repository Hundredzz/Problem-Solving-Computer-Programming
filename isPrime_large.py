"""prime"""
def main():
    """prime"""
    num = int(input())
    count = 0
    for i in range(2,int(num**0.5)+1):
        if not num % i:
            print("NO")
            count = 1
            break
    if not num or num == 1:
        print("NO")
    elif not count:
        print("YES")
main()
