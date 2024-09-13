"""Duplicate I"""
def main():
    """Duplicate I"""
    m = int(input())
    n = int(input())
    lst_m = []
    lst_f = []
    for _ in range(m):
        lst_m.append(int(input()))
    for _ in range(n):
        x = int(input())
        if x in lst_m:
            lst_f.append(x)
    lst_f.sort(reverse=True)
    if not lst_f:
        print("Nope")
    else:
        for i in lst_f:
            print(i)
main()
