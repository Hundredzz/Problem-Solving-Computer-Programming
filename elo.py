"""Elo"""
def main():
    """f"""
    ra = int(input())
    rb = int(input())
    name = input()
    if "A" in name:
        print(f"{1/(1+10**((rb-ra)/400)):.2f}")
    else:
        print(f"{1/(1+10**((ra-rb)/400)):.2f}")
main()
