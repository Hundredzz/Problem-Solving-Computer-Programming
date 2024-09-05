"""code"""
def main():
    """function"""
    first = 2000000000000
    first_pl = 0
    second = 2000000000000
    second_pl = 0
    third = 2000000000000
    third_pl = 0
    for i in range(1,9):
        num = float(input())
        if num < first:
            third_pl = second_pl
            third = second
            second_pl = first_pl
            second = first
            first_pl = i
            first = num
        elif num < second:
            third_pl = second_pl
            third = second
            second_pl = i
            second = num
        elif num < third:
            third_pl = i
            third = num
    print(f"{first_pl} {second_pl} {third_pl}")
main()
