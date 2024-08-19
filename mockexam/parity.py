"""code"""
def main():
    """function"""
    num = input()
    num_type = input()
    one = 0
    for i in num:
        if i == "1":
            one += 1
    if one % 2:
        if num_type == "Odd":
            print(num + "0")
        else:
            print(num + "1")
    else:
        if num_type == "Odd":
            print(num + "1")
        else:
            print(num + "0")
main()
