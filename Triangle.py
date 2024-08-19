"""code"""
def main():
    """function"""
    most = -2000000000000
    mid = 0
    least = 2000000000000
    a = []
    for _ in range(3):
        num = float(input())
        a.append(num)
        if num > most:
            most = num
        if num < least:
            least = num
    a.remove(most)
    a.remove(least)
    mid = a[0]
    lastnum = least ** 2 + mid **2
    if lastnum == most ** 2 or abs(round(most ** 2 - lastnum , 2)) <=0.01:
        print("Yes")
    else:
        print("No")
main()
