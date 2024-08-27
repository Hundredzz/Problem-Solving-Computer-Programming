"""restaurant"""
def main(order, promotion, proper, add):
    """function"""
    new_price_pro = (order + add) - (order + add) * (proper/100)
    if not proper:
        print("Yes")
    elif order < promotion <= order + add and order != new_price_pro:
        if new_price_pro < order:
            print("Yes", end=" ")
        else:
            print("No", end=" ")
        print(f"{abs(order - new_price_pro):.3f}")
    elif order == promotion and new_price_pro and add:
        print("No", end=" ")
        print(f"{abs((order - (order * proper /100)) - new_price_pro):.3f}")
    else:
        print("Yes")
main(float(input()),float(input()),float(input()),float(input()))
