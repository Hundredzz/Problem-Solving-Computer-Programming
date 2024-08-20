"""frame"""
def main():
    """function"""
    all_text = ""
    most_len = 0
    for _ in range(5):
        text = input().strip()
        if len(text) > most_len:
            most_len = len(text)
        all_text += text + "_"
    print("*"*(most_len+4))
    for _ in range(5):
        in_dex = all_text.find("_")
        print("* "+all_text[:in_dex]+" "*(most_len-len(all_text[:in_dex])) + " *")
        all_text = all_text[in_dex+1:]
    print("*"*(most_len+4))
main()
