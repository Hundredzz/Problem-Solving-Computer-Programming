"""Easy Histogram"""
def main():
    """histohram"""
    text =  input()
    dic = {}
    for i in text:
        if i.isalpha():
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
    dic = dict(sorted(dic.items(), key=lambda x: (x[0].upper(), x[0].isupper())))
    for i in dic:
        print(i, "=", dic[i])
main()
