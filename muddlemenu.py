"""code"""
def main():
    """function"""
    lst = []
    while True:
        text = input()
        if "DONE" in text:
            break
        if "#" in text:
            try:
                lst.insert(int(text[text.index("#")+1:])-1, text[:text.index(" #")])
            except ValueError:
                lst.append(text[:text.index(" #")])
        elif "SOMETHING'S WRONG" in text:
            lst.clear()
        elif "Can't do: " in text:
            lst.remove(text[text.index(":")+2:])
        elif "CLOSED" in text:
            lst.clear()
            break
    print(f"Full Course: {lst} Reversed: ", end = "")
    lst.reverse()
    print(lst)
main()
