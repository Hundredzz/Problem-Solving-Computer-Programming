"""code"""
def main():
    """fuction"""
    price = int(input())
    cap = int(input())
    promotion = int(input())
    money = int(input())
    cap_have = 0
    milk_have = 0
    while money >= price:
        money -= price
        milk_have += 1
        cap_have += 1
        if cap_have >= cap:
            milk_have += promotion
            cap_have = promotion
    print(milk_have)
main()
