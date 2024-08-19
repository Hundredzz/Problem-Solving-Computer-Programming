"""code"""
def main():
    """function"""
    value_price = 0
    value_weight = 0
    weight_on_one = -200000000000000000000000
    for _ in range (int(input())):
        price = float(input())
        weight = float(input())
        if weight / price > weight_on_one:
            weight_on_one = weight / price
            value_price = price
            value_weight = weight
        elif weight / price == weight_on_one and price < value_price:
            weight_on_one = weight / price
            value_price = price
            value_weight = weight
    print(f"{value_price:.2f} {value_weight:.2f}")
main()
