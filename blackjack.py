"""blackjack"""
def main():
    """blackjack cal"""
    sum_num = 0
    ace = 0
    time = int(input())
    for _ in range(time):
        num = input()
        if num in ("J", "Q", "K"):
            sum_num += 10
        elif num == "A":
            ace += 1
        else:
            sum_num += int(num)
    if ace > 0:
        for num in range(ace):
            if sum_num + 11 + (ace - (num + 1)) > 21:
                sum_num += 1
            else:
                sum_num += 11
    print(sum_num)
main()
