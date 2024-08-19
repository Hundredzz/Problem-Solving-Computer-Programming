"""code"""
def main():
    """function"""
    a_num = float(input())
    b_num = float(input())
    c_num = float(input())
    s_num = (a_num + b_num + c_num) / 2
    print(f"{(s_num*(s_num-a_num)*(s_num-b_num)*(s_num-c_num))**0.5:.3f}")
main()
