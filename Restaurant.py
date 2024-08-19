"""Restaurant"""
def main(price, price_pro, pro_per, to_getpro):
    """Promotion cal"""
    discount = (price + to_getpro) * pro_per / 100
    if discount >= to_getpro:
        print(f"Yes {discount - to_getpro:.3f}")
    else:
        print(f"No {to_getpro - discount:.3f}")
main(float(input()), float(input()), float(input()), float(input()))
