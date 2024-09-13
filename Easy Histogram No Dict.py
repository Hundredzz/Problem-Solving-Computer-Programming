"""Easy Histogram No Dict"""
def main():
    """histogram"""
    text = input()
    lst = []
    new_lst = []
    lst.extend(text)
    lst.sort(key=lambda x: (x.upper(), x.isupper()))
    for i in lst:
        if i.isalpha() and not i in new_lst:
            new_lst.append(i)
    for j in new_lst:
        print(j,"=",text.count(j))
main()
