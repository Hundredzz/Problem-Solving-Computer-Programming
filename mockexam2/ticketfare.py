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
    if f < 1 or g < 1 or f > n or g > n:
        print("Error")
        return
    if abs(g-f) <= a:
        price = b
    elif abs(abs(g-f)-a) <= c:
        price = b
        price += d * abs(abs(f-g)-a)
    else:
        price = b
        price += d * c
        price += e * abs(abs(abs(f-g)-a) -c)
    print(price)
main()
