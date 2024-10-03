"""code"""
def main():
    """function"""
    text = input()
    new_text = ""
    state = True
    if not "<" in text or not ">" in text:
        print(text.split())
    else:
        for i in text:
            if i == "<":
                state = False
            elif i == ">":
                state = True
                new_text += " "
            elif state:
                new_text += i
        print(new_text.split())
main()
