"""code"""
def main():
    """function"""
    price = int(input())
    promo_count = int(input())
    promo_price = int(input())
    want = int(input())
    if not promo_count:
        print(price * want)
    elif not want:
        print(0)
    else:
        first_set = price * promo_count + promo_price
        one_set = price * (promo_count - 1) + promo_price
        all_set = (want - (promo_count + 1)) // promo_count
        sase = want - all_set * promo_count - (promo_count +1)
        print(first_set +one_set * all_set + price * sase)
main()
