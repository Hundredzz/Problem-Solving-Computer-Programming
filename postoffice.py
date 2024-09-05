"""code"""
def son_check(num):
    """function"""
    price = 13
    if 0<num<=10:
        price += 16
    elif num <=20:
        price += 18
    elif num <=100:
        price += 23
    elif num <=250:
        price += 28
    elif num <=500:
        price += 33
    elif num <=1000:
        price += 48
    elif num <=2000:
        price += 68
    return price
def box_check(num):
    """function"""
    price = 15
    if 0<num<=500:
        price+=45
    elif num <= 1000:
        price += 55
    elif num <= 2000:
        price += 70
    return price
def main():
    """function"""
    son = int(input())
    box = int(input())
    price = 0
    for _ in range(son):
        num = float(input())
        price += son_check(num)
    for _ in range(box):
        num = float(input())
        price += box_check(num)
    print(price)
main()
