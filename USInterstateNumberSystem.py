"""a"""
def main():
    """b"""
    num = int(input())
    num = str(num)
    if int(num) < 5 or int(num) > 995:
        print("Others")
    elif len(num) <= 2:
        if num[-1] == "0":
            print("Horizontal Major Interstate")
            print(f"I-{num}")
        elif num[-1] == "5":
            print("Vertical Major Interstate")
            print(f"I-{num}")
        else:
            print("Others")
    elif len(num) == 3:
        if int(num[1:]) < 5:
            print("Others")
        else:
            if num[-1] == "0" or num[-1] == "5":
                if int(num[0]) % 2:
                    print("Odd Minor Interstate")
                else:
                    print("Even Minor Interstate")
                print(f"I-{int(num[1:])}")
            else:
                print("Others")
main()
