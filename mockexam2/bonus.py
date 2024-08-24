"""bonus"""
def main():
    """function"""
    salary = int(input())
    year = int(input())
    month = int(input())
    if month > 9:
        year += 1
    if year > 20:
        year = 20
    bonus =  salary * year
    bonus = max(bonus, 5000)
    bonus = min(bonus,1000000)
    print(bonus)
main()
