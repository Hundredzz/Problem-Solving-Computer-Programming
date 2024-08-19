"""code"""
def main(price,year):
    """inflation_cal"""
    print(f"{int((price*(1+0.0381)**year)*100)/100}")
main(float(input()),int(input()))
