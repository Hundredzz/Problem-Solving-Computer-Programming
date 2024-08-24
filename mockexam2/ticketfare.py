"""code"""
def main():
    """function"""
    n= int(input())
    a= int(input())
    b= int(input())
    c= int(input())
    d= int(input())
    e= int(input())
    f= int(input())
    g= int(input())
    price = 0
    if f < 1 or g > n or f > n or g < 1:
        print("Error")
    else:
        if abs(g-f) <= a:
            price = b
        elif abs(g-f) <= a+c:
            price = b
            price += d *((a+c)-abs((g-(f-1))))
        elif abs(g-f) > a+c:
            price = b
            price += d * c
            price += e*(abs((g-f)) - (a+c))
    if price:
        print(price)
main()
