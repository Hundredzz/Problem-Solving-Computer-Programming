"""code"""
def main():
    """function"""
    day = input()
    age = float(input())
    height = float(input())
    if age < 14:
        if height < 90:
            print("FREE")
        elif height <= 140:
            if day == "Children Day":
                print("FREE")
            else:
                print("PAY")
        else:
            print("PAY")
    elif age >= 60:
        if day == "Senior Day":
            print("FREE")
        else:
            print("PAY")
    else:
        print("PAY")
main()
