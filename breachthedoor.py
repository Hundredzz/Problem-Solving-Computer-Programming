"""code"""
import re
def main():
    """function"""
    final = []
    text = input()
    text = re.sub(r'[^A-Za-z\s]', '', text)
    lst = text.split()
    for i in lst:
        if len(i) > 6:
            final.append(i)
    print(" ".join(final))
main()
