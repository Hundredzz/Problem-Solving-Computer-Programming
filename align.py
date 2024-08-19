"""code"""
def main(space,direct,text):
    """function"""
    if direct == "left":
        print(text+" "*(space-len(text)))
    elif direct == "center":
        if (space - len(text)) % 2:
            text = " " + text
        print(text.center(space))
    else:
        print(" "*(space-len(text))+text)
main(int(input()),input(),input())
