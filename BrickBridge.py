"""code"""
def main():
    """function"""
    small_brick = int(input())
    large_brick = int(input())
    goal = int(input())
    large_brick_want = goal // 5
    if large_brick_want > large_brick:
        large_brick_want = large_brick
    small_brick_want = goal - large_brick_want * 5
    if small_brick_want > small_brick:
        print(-1)
    else:
        print(small_brick_want)
main()
