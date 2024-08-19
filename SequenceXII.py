"""code"""
def print_pattern(num, first, last, num_print, i):
    """function"""
    num_print2 = 0
    for j in range(num + num-1):
        if j in (first, last):
            print(f"{num_print:02}",end=" ")
        else:
            if j == num - 1:
                num_print2 = i
            elif j < first:
                num_print2 = num - (first - j)
            elif first < j < last:
                if j < num:
                    num_print2 = num - (j - first)
                else:
                    num_print2 = num - (last - j)
            elif j > last:
                num_print2 = num - (j - last)
            print(f"{num_print2:02}", end=" ")
def main():
    """function"""
    num = int(input())
    first = -1
    last = num + num-1
    num_print = num
    i_value = 0
    for i in range(num+ num -1):
        if i < num:
            first += 1
            last -= 1
            i_value = i+1
            print_pattern(num, first, last, num_print, i_value)
        else:
            first -= 1
            last += 1
            i_value -=1
            print_pattern(num, first, last, num_print, i_value)
        print()
main()
