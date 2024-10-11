"""code"""
def main():
    """function"""
    lst = []
    dis = []
    max_dis = 20000000000
    place = 0
    distance = int(input())
    play = int(input())
    for _ in range(play):
        x = input()
        lst.append(x[:x.find(" ")])
        dis.append(x[x.find(" ")+1:])
    for i in range(play):
        y = (distance-int(dis[i]))/int(lst[i])
        if y == max_dis:
            if lst[i] > lst[place-1]:
                max_dis = y
                place = i+1
        elif y < max_dis:
            max_dis = y
            place = i+1
    print(place)
main()
