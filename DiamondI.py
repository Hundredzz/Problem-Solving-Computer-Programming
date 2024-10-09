"""code"""
def main():
    """function"""
    lst = []
    sum_lst = []
    num = 0
    row = int(input())
    column = int(input())
    for _ in range(row):
        lst.append(input().split())
    for i in range(column):
        for j in lst:
            num += int(j[i])
        sum_lst.append(num)
        num = 0
    print(max(sum_lst))
main()
