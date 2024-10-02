"""code"""
def main():
    """funct"""
    first = []
    first.extend(input())
    second = []
    second.extend(input())
    for i in range(max(len(first), len(second))+1):
        print("".join(second[:i])+"".join(first[i:]))
main()
