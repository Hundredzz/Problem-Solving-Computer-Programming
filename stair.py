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
        if all_height > height_can:
            kao += count - 1
            all_height -= height_can
            count = 1
        height = int(input())
        if height > height_can:
            kao = 0
            break
        elif height == height_can:
            kao += 1
        else:
            all_height += height_can
            count += 1
            old_height = all_height
main()
