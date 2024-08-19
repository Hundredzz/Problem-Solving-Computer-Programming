"""RockPaperScissor"""
def main(match):
    """winner"""
    naia = 0
    naib = 0
    char = ""
    for i in match:
        char += i
        if len(char) == 2:
            if char in ("RS","SP","PR"):
                naia += 1
            elif char in ("SR","PS","RP"):
                naib += 1
            char = ""
    if naia > naib:
        print(f"A win {naia}-{naib}")
    elif naib > naia:
        print(f"B win {naib}-{naia}")
    else:
        print(f"DRAW {naia}")
main(input())
