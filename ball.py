"""code"""
def main():
    """ball_bouce_cal"""
    height = float(input())
    num = 0
    while True:
        height *= 3/5
        if height < 0.01:
            break
        num += 1
    print(num)
main()
