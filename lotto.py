"""lottery"""
def near(first):
    """near"""
    if first == "999999":
        near_f = "000000" + " " + "999998"
    elif first == "000000":
        near_f = "000001" + " " + "999999"
    else:
        if first.rfind("0") != -1 and first.rfind("0") != 5:
            near_f = first[:first.rfind("0")+1] + str(int(first[first.rfind("0")+1:]) - 1) + " "\
+ first[:first.rfind("0")+1] + str(int(first[first.rfind("0")+1:])+1)
        else:
            near_f = str(int(first) - 1) + " " +str(int(first)+1)
    return near_f
def main():
    """function"""
    first = input()
    near_f = near(first)
    two_l = input()
    three_f = input() + " " + input()
    three_l = input() + " " + input()
    lotto = input()
    prize = 0
    if lotto == first:
        prize += 6000000
    if lotto[-2:] in two_l:
        prize += 2000
    if lotto[:3] in three_f:
        prize += 4000
    if lotto[-3:] in three_l:
        prize += 4000
    if lotto in near_f:
        prize += 100000
    print(prize)
main()
