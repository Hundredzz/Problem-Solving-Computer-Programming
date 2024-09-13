"""MissingNumber"""
def main():
    """MissingNumber"""
    n = int(input())
    setA = set()
    setB = set()
    for i in range (1,n+1):
        setA.add(i)
    while True:
        x = int(input())
        if not x:
            break
        setB.add(x)
    for i in sorted(setA - setB):
        print(i)
main()
