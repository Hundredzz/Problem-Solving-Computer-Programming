"""Difference"""
def main():
    """Difference"""
    n = int(input())
    m = int(input())
    setA = set()
    setB = set()
    for _ in range (n):
        setA.add(int(input()))
    for _ in range(m):
        setB.add(int(input()))
    for i in sorted(setA.difference(setB)):
        print(i,end=" ")
main()
