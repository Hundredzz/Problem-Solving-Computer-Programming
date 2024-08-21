"""One For All"""
def main():
    """All For One"""
    num = int(input())
    text = ""
    for i in range(num):
        name = input()
        if i % 2:
            text += "*"*i
        else:
            text += "-"*i
        text += name
        if i == num-1:
            text += "_"+str(num)
    print(text)
main()
