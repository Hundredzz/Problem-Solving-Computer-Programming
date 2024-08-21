"""lottery"""
def near(first):
    """near"""
    near_c1 = ""
    near_c2 = ""
    if first == "999999":
        near_f = "000000" + " " + "999998"
    elif first == "000000":
        near_f = "000001" + " " + "999999"
    else:
        if first.rfind("0") != -1 and first.rfind("0") != 5:
            near_f = first[:first.rfind("0")+1] + str(int(first[first.rfind("0")+1:]) - 1) + " "\
+ first[:first.rfind("0")+1] + str(int(first[first.rfind("0")+1:])+1)
        else:
            near_c1 = str(int(first) - 1)
            near_c1 = "0"*(6-len(near_c1)) + near_c1
            near_c2 = str(int(first)+1)
            near_c2 = "0"*(6-len(near_c2)) + near_c2
            near_f = near_c1 + " " + near_c2
    return near_f
def main():
    """function"""
    first = input()
    near_f = near(first)
    two_l = input()
    three_f1 = input()
    three_f2 = input()
    three_l1 = input()
    three_l2 = input()
    lotto = input()
    prize = 0
    if lotto == first:
        prize += 6000000
    if lotto in near_f:
        prize += 100000
    if lotto[-2:] == two_l:
        prize += 2000
    if lotto[:3] == three_f1:
        prize += 4000
    if lotto[:3] == three_f2:
        prize += 4000
    if lotto[-3:] == three_l1:
        prize += 4000
    if lotto[-3:] == three_l2:
        prize += 4000
    print(prize)
main()
