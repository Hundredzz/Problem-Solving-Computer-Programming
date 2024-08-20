"""phonenum"""
def main():
    """function"""
    number = input()
    nation = input()
    if nation == "International":
        number = number.replace("0","+66",1)
    print(number[:-8], number[-8:-4], number[-4:])
main()
