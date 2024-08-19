"""stair"""
def main():
    """function"""
    height_can = int(input())
    stair_num = int(input())
    all_height = 0
    old_height = 0
    height = 0
    kao = 0
    check = True
    for _ in range(stair_num):
        height = int(input())
        if all_height > height_can:
            kao += 1
            all_height -= old_height
            if height + all_height > height_can:
                kao += 1
                all_height = 0
        elif all_height == height_can and height_can:
            kao += 1
            all_height = 0
        if height > height_can:
            kao = 0
            check = False
            break
        if height == height_can:
            kao += 1
        else:
            old_height = all_height
            all_height += height
    if check:
        if all_height > height_can:
            kao += 2
        elif 0 < all_height <= height_can:
            kao += 1
    if kao:
        print(kao)
    else:
        print("NO")
main()
