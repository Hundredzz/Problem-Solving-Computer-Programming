"""code"""
def tax(income, tax_pay):
    """recursive tax"""
    if income > 4000000:
        tax_pay = (income - 4000000)*0.35
        income = 4000000
    elif income > 2000000:
        tax_pay = (income - 2000000)*0.30
        income = 2000000
    elif income > 1000000:
        tax_pay = (income - 1000000)*0.25
        income = 1000000
    elif income > 750000:
        tax_pay = (income - 750000)*0.20
        income = 750000
    elif income > 500000:
        tax_pay = (income - 500000)*0.15
        income = 500000
    elif income > 300000:
        tax_pay = (income - 300000)*0.10
        income = 300000
    elif income > 150000:
        tax_pay = (income - 150000)*0.05
        income = 150000
    else:
        return 0
    return tax_pay + tax(income, 0)
def main():
    """function"""
    income = int(input())
    print(int(tax(income, 0)))
main()
