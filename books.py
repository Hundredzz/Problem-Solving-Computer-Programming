"""code"""
import math
def main():
    """function"""
    book = int(input())
    page = int(input())
    read = 0
    day = 0
    x = int(input())
    y = int(input())
    a = 0
    while book > 0:
        if math.ceil(page * (x/y)) >= page:
            day += book
            break
        if read + math.ceil(page * (x/y)) >=page:
            book -= 1
            read = 0
        else:
            read+=math.ceil(page * (x/y))
        a += (x/y)
        day += 1
        x += 1
        y += 1
    print(day)
main()
