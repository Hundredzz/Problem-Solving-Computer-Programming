"""code"""
def main():
    """function"""
    name = input()
    thai = input()
    home = input()
    age = float(input())
    income = float(input())
    bank = float(input())
    check = thai in ("Yes","True") and home in ("Yes","True") and age >=16\
and income <= 840000 and bank <= 500000
    if check:
        print(f"Congratulations! {name} is qualified to receive\
 a digital wallet amount of 10,000 baht, sponsored by all taxpayers in Thailand.")
    else:
        print(f"Unfortunately, {name} is not qualified.")
main()
