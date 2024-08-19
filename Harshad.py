"""code"""
def main():
    """function"""
    for _ in range(10):
        og_num = input()
        new = str(abs(int(og_num)))
        num = list(map(int, new))
        og_num = int(og_num)
        num = sum(num)
        if not og_num:
            print("No")
        elif not og_num % num:
            print("Yes")
        else:
            print("No")
main()
