"""code"""
def main():
    """function"""
    text = input()
    for i in range(1,len(text)*2):
        if i < len(text):
            print(" " * (len(text) - i)+text[:i])
        else:
            print(text[i - (len(text)):])
main()
