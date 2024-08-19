"""code"""
import math
def main():
    """function"""
    x = float(input())
    y = float(input())
    r = float(input())
    xn = float(input())
    yn = float(input())
    r2 = float(input())
    d = math.sqrt((xn-x)**2+(yn-y)**2)
    if d<r+r2:
        print("Yes")
    else:
        print("No")
main()
