"""stair"""
def main():
    """function"""
    height_can = int(input())
    stair_num = int(input())
    all_height = 0
    kao = 0
    check = True
    for _ in range(stair_num):
        height = int(input())
        all_height += height
        if height > height_can:
            check = False
        elif all_height > height_can:
            kao += 1
            all_height = height
        elif all_height == height_can:
            kao += 1
            all_height = 0
    if all_height:
        kao += 1
    if check:
        print(kao)
    else:
        print("NO")
main()
