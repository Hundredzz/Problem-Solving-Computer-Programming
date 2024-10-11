"""code"""
def main():
    """function"""
    count = 0
    lst = []
    for _ in range(int(input())):
        time = float(input())
        x = int(input())
        for _ in range(x):
            lst.append(float(input()))
        lst.sort()
        for i in lst:
            time -= i
            if time >= 0:
                count += 1
        print(count)
        count = 0
        lst.clear()
main()
