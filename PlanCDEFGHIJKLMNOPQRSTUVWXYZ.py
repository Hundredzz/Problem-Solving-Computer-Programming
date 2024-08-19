"""code"""
"""โค้ดไม่ดี"""
def main():
    """main"""
    text = input()
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    most = 0
    mid = 0
    least = 0
    if num1 >= num2 and num1 >= num3:
        most = num1
    elif num2 >= num1 and num2 >= num3:
        most = num2
    else:
        most = num3
    if num1 <= num2 and num1 <= num3:
        least = num1
    elif num2 <= num1 and num2 <= num3:
        least = num2
    else:
        least = num3
    if num2<num1<num3 or num3<num1<num2:
        mid = num1
    elif num1<num2<num3 or num3<num2<num1:
        mid = num2
    else:
        mid = num3
    if text == "Ascend":
        print(f"{least:.2f}, {mid:.2f}, {most:.2f}")
    else:
        print(f"{most:.2f}, {mid:.2f}, {least:.2f}")
main()
