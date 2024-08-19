"""kayak"""
def main():
    """min sum"""
    amount = int(input())
    kayak = amount-1
    text = input()
    sum_weight = 0
    sum_weight2 = 0
    weight = text.split()
    int_weight = []
    diff = []
    diff2 = []
    for num in weight:
        int_weight.append(int(num))
    int_weight.sort()
    for num in range(0, len(int_weight), 2):
        diff.append(int_weight[num+1] - int_weight[num])
    for num in range(1, len(int_weight) -1 , 2):
        diff2.append(int_weight[num+1] - int_weight[num])
    for _ in range(kayak):
        sum_weight += min(diff)
        diff.remove(min(diff))
    for _ in range(kayak):
        sum_weight2 += min(diff2)
        diff2.remove(min(diff2))
    if sum_weight2 < sum_weight:
        print(sum_weight2)
    else:
        print(sum_weight)
main()
