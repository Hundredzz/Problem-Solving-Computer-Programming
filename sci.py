"""code"""
def main():
    """function"""
    num = input()
    num1 = ""
    zero = True
    for i in num:
        if i != 0 or i !=".":
            zero = False
            break
    if zero:
        num = 0
    elif " x 10^" in num:
        if "-" in num:
            num = ("0"* int(num[num.find(" x 10^")+7:])) + num[0] + num[2:num.find(" x 10^")]
            num = num[0] + "." + num[1:]
        else:
            num = num[:num.find(" x 10^")] + ("0"* (int(num[num.find(" x 10^")+6:])-len(num[num.find(".")+1:num.find(" x 10^")])))
            num = num[0]+num[2:]
    else:
        if "." in num and float(num) > 1:
            first = num.find(".")
            num = num[:first] + num[first+1:]
            num = num[0] + "." + num[1:] + " x 10^"+ str(len(num[1:first]))
        elif "." in num and float(num) < 1:
            first = num.find(".")
            num1 = str(int(num[:first] + num[first+1:]))
            num = num1[0] + "." + num1[1:] + " x 10^-"+ str(len(num)-len(num1)-1)
        else:
            num = str(float(num[0]+"."+num[1:])) + " x 10^"+ str(len(num[1:]))
    print(num)
main()
