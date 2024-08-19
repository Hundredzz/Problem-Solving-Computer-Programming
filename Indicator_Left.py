"""Indicator_Left"""
def main():
    """Loop"""
    width = int(input())
    height = int(input())
    start = int(height //2)
    for num in range(-start,start+1):
        print(" " * abs(num) + "*" * width)
main()
