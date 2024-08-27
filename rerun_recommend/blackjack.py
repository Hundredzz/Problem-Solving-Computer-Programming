"""code"""
def main(num):
    """function"""
    point = 0
    ace = 0
    for _ in range(num):
        card = input()
        if card == "A":
            ace += 1
        elif card.isnumeric():
            point += int(card)
        else:
            point += 10
    if point + 11 + (ace-1) <= 21 and ace:
        point += 11 + (ace-1)
    else:
        point += ace
    print(point)
main(int(input()))
