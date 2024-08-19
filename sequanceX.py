"""code"""
def main():
    """function"""
    ix = int(input())
    for i in range(ix,0,-1):
        num = 1
        for j in range(1,ix+1*(ix-i+1)):
            if j < i:
                print("  ",end =" ")
            else:
                if j > ix:
                    num -= 1
                    print(f"{num:02}", end=" ")
                else:
                    print(f"{num:02}", end=" ")
                    if j == ix:
                        continue
                    num += 1
        print()
    for i in range(1,ix):
        num = 1
        for j in range(1,ix+1*(ix-i)):
            if j <= i:
                print("  ",end =" ")
            else:
                if j > ix:
                    num -= 1
                    print(f"{num:02}", end=" ")
                else:
                    print(f"{num:02}", end=" ")
                    if j == ix:
                        continue
                    num += 1
        print()
main()
