"""code"""
def main():
    """function"""
    text = " "+input()+" "
    sunin = text.find(" Sun ")
    countl = 0
    maxl = 0
    minr = 0
    countr = 0
    if not sunin:
        print(f"Hot: {text[5:text.find(' ' , 5)]}")
        print(f"Cool: {text[text.rfind(' ',0,-1)+1:-1]}")
    elif sunin == len(text)-5:
        print(f"Hot: {text[text.rfind(' ',0,-5)+1:-5]}")
        print(f"Cool: {text[1:text.find(' ' , 1)]}")
    else:
        maxl = text.rfind(" ", 0, sunin)+1
        minr = sunin + 5
        print(f"Hot: {text[maxl:sunin]} {text[minr:text.find(' ',minr)]}")
        print("Cool:", end = " ")
        countl = text[1:sunin+1].count(" ")
        countr = text[sunin+5:].count(" ")
        if countl == countr:
            print(f"{text[1:text.find(' ',1)]} {text[text.rfind(' ', 0, -1)+1:-1]}")
            return
        if countl > countr:
            print(f"{text[1:text.find(' ',1)]}")
            return
        print(f"{text[text.rfind(' ', 0, -1)+1:-1]}")
main()
