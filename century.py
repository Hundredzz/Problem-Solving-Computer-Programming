"""century"""
def main():
    """century"""
    for _ in range(int(input())):
        year = input()
        if "B.E." in year:
            year = str(int(year[4:])-543)
        else:
            year = str(int(year[4:]))
        if int(year) > 100 and int(year[-2:]) > 0:
            print(int(year[:-2])+1)
        elif int(year) > 100:
            print(int(year[:-2]))
        elif int(year) > 0:
            print(1)
        else:
            print("ERROR")
main()
