"""longer"""
import math
def main():
    """function"""
    r_value = float(input())
    a_value = float(input())
    b_value = float(input())
    circle = 2 * math.pi * r_value
    rec = (2*a_value)+ (2*b_value)
    if circle > rec:
        print("Circle is longer")
    elif circle < rec:
        print("Rectangle is longer")
    else:
        print("Equal")
    print(f"{abs(circle - rec):.5f}")
main()
