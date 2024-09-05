"""code"""
def low_to_high(num):
    """fuction"""
    first = "9"
    second = "9"
    third = "9"
    fourth = "9"
    for i in num:
        if i < first:
            fourth = third
            third = second
            second = first
            first = i
        elif i < second:
            fourth = third
            third = second
            second = i
        elif i < third:
            fourth = third
            third = i
        else:
            fourth = i
    return first + second + third + fourth
def main():
    """finction"""
    num = int(input())
    count = 0
    while num != 6174:
        low = low_to_high(str(num))
        high = low[::-1]
        num = int(high) - int(low)
        if len(str(num)) < 4:
            num = str(num)
            num += "0"*(4-len(num))
            num = int(num)
        count += 1
    print(count)
main()
