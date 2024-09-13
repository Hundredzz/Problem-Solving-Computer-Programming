"""code"""
def main():
    """function"""
    time = int(input())
    price_pro = int(input())
    stamp_tim = int(input())
    stamp_pro = int(input())
    discount = int(input())
    ne_discount = 0
    stamp = 0
    all_price = 0
    for _ in range(time):
        num = int(input())
        if stamp >= stamp_pro:
            while ne_discount< num:
                if stamp < stamp_pro:
                    break
                stamp -= stamp_pro
                ne_discount += discount
            num -= ne_discount
            ne_discount = 0
            if num < 0:
                num = 0
            all_price += num
        else:
            all_price += num
        stamp += (num // price_pro) * stamp_tim
    print(all_price)
    print(stamp)
main()
