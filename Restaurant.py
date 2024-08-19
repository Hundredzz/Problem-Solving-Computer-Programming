"""Restaurant"""
def main(price, price_pro, pro_per, to_getpro):
    """Promotion cal"""
    last_price = price + to_getpro
    if price_pro < last_price:
        pro_discount = last_price * pro_per / 100
        value_price = abs(price-(last_price - pro_discount))
        if last_price == pro_discount:
            print("Yes")
        elif last_price - pro_discount < price:
            print(f"Yes {value_price:.3f}")
        elif last_price - pro_discount > price:
            print(f"No {value_price:.3f}")
    else:
        print("Yes")
main(float(input()), float(input()), float(input()), float(input()))
