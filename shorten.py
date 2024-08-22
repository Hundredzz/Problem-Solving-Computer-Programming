"""shorten"""
def main():
    """function"""
    num = 0
    old_num = 0
    first = 0
    con = False
    out = ""
    while num != -1:
        num = int(input())
        if not first:
            first = num
        elif num - old_num == 1:
            con = True
        elif num - old_num != 1:
            if con:
                out += "  " + str(first) + "-" + str(old_num)
                first = num
                con = False
            else:
                out += "  " + str(first)
                first = num
        old_num = num
    out = out.strip()
    print(out.replace("  ",", "))
main()
