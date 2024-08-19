"""Cha Cha Cha"""
import math
def main():
    """function"""
    day = int(input())
    all_hour = 0
    for _ in range(day):
        hour = float(input())
        all_hour += math.ceil(hour)
    print(int(8720*all_hour))
main()
