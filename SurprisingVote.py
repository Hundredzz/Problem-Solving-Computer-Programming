"""code"""
def main():
    """function"""
    score = float(input())
    high = float(input())
    if high == score or high *2 >= score:
        lowestnum = 0
    else:
        lowestnum = score - 2* high
    if high >score or high - lowestnum > 2:
        print("Surprising")
    else:
        print("Not surprising")
main()
