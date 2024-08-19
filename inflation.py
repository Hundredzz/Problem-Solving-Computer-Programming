"""code"""
def main(price,year):
    """inflation_cal"""
    price = int(price*100)
    while year:
        price += int((price * 381)//10000)
        year -= 1
    print(f"{price//100}.{price%100:>02}")
main(float(input()),int(input()))
