"""code"""
def main():
    """func"""
    nums = int(input())
    nump = int(input())
    _ = input()
    _ = input()
    wolabtop = input()
    hd = input()
    uhd = input()
    mobi = 0
    bas = 0
    stan = 0
    prem = 0
    price = 0
    while True:
        if nums <= 0 and nump <= 0:
            break
        if ((nums >= 3 or nump >=3) and (wolabtop == "Yes" or hd == "Yes")) or uhd == "Yes":
            prem += 1
            nums -= 4
            nump -= 4
        elif ((nums >= 2 or nump >=2) and wolabtop == "Yes") or hd == "Yes":
            stan += 1
            nump -= 2
            nums -= 2
        elif (nums >= 1 or nump >=1) and wolabtop == "Yes":
            bas += 1
            nums -= 1
            nump -= 1
        else:
            mobi += 1
            nums -= 1
            nump -= 1
    if prem:
        price += prem * 419
        print(f"Premium x {prem}")
    if stan:
        price += stan * 349
        print(f"Standard x {stan}")
    if bas:
        price += bas * 279
        print(f"Basic x {bas}")
    if mobi:
        price += mobi*99
        print(f"Mobile x {mobi}")
    print(f"Total = {price} THB")
main()
