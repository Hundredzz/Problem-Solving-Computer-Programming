"""code"""
def main(day, age, height):
    """function"""
    first = age < 14 and ((day == "Children Day" and height <= 140) or height < 90)
    second = age >= 60 and day == "Senior Day"
    if first or second:
        print("FREE")
    else:
        print("PAY")
main(input(), float(input()), float(input()))
