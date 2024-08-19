"""code"""
def print_pattern(num, first, last, num_print):
    """function"""
    num_print2 = 1
    for j in range(num + num-1):
        if first<=j<last:
            print(f"{num_print:02}",end=" ")
        else:
            if j < num:
                print(f"{num_print2:02}",end=" ")
                num_print2+=1
            else:
                num_print2-=1
                print(f"{num_print2:02}",end=" ")
def main():
    """function"""
    num = int(input())
    first = -1
    last = num + num
    num_print = 0
    for i in range(num+ num-1):
        if i < num:
            first += 1
            last -= 1
            num_print +=1
            print_pattern(num, first, last, num_print)
        else:
            first -= 1
            last += 1
            num_print -=1
            print_pattern(num, first, last, num_print)
        print()
main()
