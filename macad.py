"""macad"""
def main():
    """function"""
    text = input().upper()
    Hex = "0123456789ABCDEF"
    a = 0
    sym = ""
    count = 0
    countlim = 200000000
    for i in Hex:
        a += text.count(i)
    if a != 12 or not text[-1] in Hex:
        print("ERROR")
        return
    for i in text:
        if (i in ":-" and count == 2) and (i == sym or not sym):
            if not sym:
                sym = i
                countlim = 2
            count = 0
            continue
        if (i == "." and count == 4) and (i == sym or not sym):
            if not sym:
                sym = i
                countlim = 4
            count = 0
            continue
        if i in Hex and count < countlim:
            count += 1
            continue
        print("ERROR")
        return
    if "-" in text:
        print("VALID 1")
    elif ":" in text:
        print("VALID 2")
    elif "." in text:
        print("VALID 3")
    else:
        print("ERROR")
main()
