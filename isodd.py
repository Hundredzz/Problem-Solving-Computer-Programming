"""code"""
def is_odd(num):
    """function"""
    if num % 2:
        return "True"
    return "False"

def main():
    """function"""
    num = int(input())
    print(is_odd(num))

main()
