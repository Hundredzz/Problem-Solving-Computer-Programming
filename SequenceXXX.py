"""Sequence"""
def main(size, among):
    """loop"""
    for i in range(size):
        for _ in range(among):
            if not i or i == size - 1:
                print("*"*size, end=" ")
            else:
                for k in range(size):
                    if not k or k == size - 1:
                        print("*", end="")
                    elif k in (i, size - 1 - i):
                        print("*", end="")
                    else:
                        print(" ", end="")
                print(" ",end="")
        print()
main(int(input()), int(input()))
