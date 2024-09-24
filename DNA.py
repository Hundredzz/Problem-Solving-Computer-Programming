"""code"""
def main():
    """function"""
    text1 = input()
    text2 = input()
    longtext = ""
    lontext = ""
    if len(text1) > len(text2):
        text1,text2 = text2,text1
    for i in text1:
        lontext += i
        if i in "ACGT":
            if lontext in text2:
                if len(lontext) > len(longtext):
                    longtext = lontext
                continue
            lontext = lontext[1:]
        else:
            print("Error")
            return
    for i in text2:
        if i in "ACGT":
            continue
        print("Error")
        return
    if longtext:
        print(longtext)
    else:
        print("None")
main()
