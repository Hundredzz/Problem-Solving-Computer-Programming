"""cat"""
def main():
    """parade"""
    lst = []
    dic = {}
    while True:
        text = input()
        if text == "END":
            break
        if text == "IT'S A DOG":
            lst.pop()
        else:
            lst.extend(text.split(", "))
    new_lst = lst.copy()
    new_lst.sort()
    for i in new_lst:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for i in dic.items():
        print(i[0], lst.index(i[0])+1, i[1])
main()
