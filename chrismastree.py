"""code"""
def main(leave,wood):
    """loop"""
    space = leave-1
    for i in range(1,leave * 2 +1,2):
        for _ in range(space):
            print(" ", end="")
        print("*"*i)
        space-=1
    for _ in range(wood):
        for _ in range(leave-2):
            print(" ", end="")
        print("---")
main(int(input()),int(input()))
