'''squid'''
def main():
    '''game'''
    a = 0
    b = 0
    for _ in range(10):
        a+=int(input())
    for _ in range(10):
        b+=int(input())
    if a < b:
        print("A")
    elif a == b:
        print("AB")
    else:
        print("B")
main()
