"""code"""
def main():
    """function"""
    price = float(input())
    ft_per = float(input())
    sd_per = float(input())
    pro = float(input())
    want = int(input())
    pro_a = price + (price-(price * ft_per/100))*(want-1)
    pro_b = price * want
    if pro_b >= pro:
        pro_b -= pro_b*(sd_per/100)
    if pro_b <= pro_a:
        print(2)
        print(f"{pro_b:.2f}")
    else:
        print(1)
        print(f"{pro_a:.2f}")
main()
