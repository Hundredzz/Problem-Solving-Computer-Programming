"""code"""
def main():
    """function"""
    alice = int(input())
    bob = int(input())
    icecream = int(input())
    if abs(icecream - alice) == abs(icecream -bob):
        print(f"Sundaes {abs(icecream - alice)}")
    elif abs(icecream - alice) < abs(icecream - bob):
        print(f"Alice {abs(icecream - alice)}")
    else:
        print(f"Bob {abs(icecream -bob)}")
main()
