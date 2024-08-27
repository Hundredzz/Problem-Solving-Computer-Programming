"""code"""
def chicken(count):
    """recursive"""
    weight = int(input())
    num = 0
    if 50 <= weight <= 70:
        num = 1
    if count > 1:
        return num + chicken(count-1)
    return num
def main():
    """function"""
    num = 0
    num = chicken(24)
    print(num)
main()
