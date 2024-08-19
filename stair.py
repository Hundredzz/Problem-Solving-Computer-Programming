"""stair"""
def main():
    """function"""
    height_can = int(input())
    stair_num = int(input())
    all_height = 0
    old_height = 0
    count = 0
    height = 0
    kao = 0
    for _ in range(stair_num):
        height = int(input())
        all_height += height
        if height > height_can:
            kao = 0
            break
        if all_height > height_can and old_height:
            kao += count
            all_height -= old_height
            count = 1
            old_height = 0
        elif all_height == height_can and not old_height:
            kao += 1
            all_height = 0
            count = 0
            old_height = 0
        elif all_height == height_can:
            kao += 1
            count = 0
            old_height = 0
            all_height = 0
        elif all_height < height_can:
            count += 1
            old_height += height
        elif all_height > height_can:
            kao = 0
            break
    if kao:
        print(kao)
    else:
        print("NO")
main()
