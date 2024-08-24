"""homerun"""
def main():
    """function"""
    sanam = int(input())
    batter = float(input())
    homerun = 0
    for _ in range(sanam):
        distance = float(input())
        if batter > distance:
            homerun += 1
    print(homerun)
main()
