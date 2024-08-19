"""code"""
def main(num):
    """Nloop"""
    for i in range(num):
        for j in range(num):
            if not j or j == num - 1 or j == i:
                print("*", end="")
            else:
                print(" ", end="")
        print()
main(int(input()))
