"""code"""
def main():
    """function"""
    people = int(input())
    lift_can = float(input())
    all_weight = 0
    child = 1
    for _ in range(people):
        age = int(input())
        all_weight+=float(input())
        if age >= 12:
            child = 0
    if (child and people) or all_weight > lift_can:
        print("Not Safe")
    else:
        print("Safe")
main()
