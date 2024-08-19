"""code"""
def is_even(num):
    """function"""
    if not num % 2:
        print(num)

def main():
    """function"""
    for _ in range(8):
        num = int(input())
        is_even(num)

main()
