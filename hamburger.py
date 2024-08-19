"""hamburger"""
def main():
    """hamburger slide screen"""
    top = int(input())
    bot = int(input())
    pork = (top + bot) * 2
    print("|" * top + "*" * pork + "|" * bot)
main()
