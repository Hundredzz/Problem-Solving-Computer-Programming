"""bad"""
def main():
    """keyboard"""
    text = input()
    new_text = ""
    for i in text:
        if i == "i":
            new_text+="o"
        elif i == "o":
            new_text+="i"
        elif i == "I":
            new_text+="O"
        elif i == "O":
            new_text+="I"
        else:
            new_text += i
    print(new_text)
main()
