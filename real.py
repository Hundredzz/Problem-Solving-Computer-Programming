"""real"""
def inp():
    """input"""
    text = ""
    for _ in range(8):
        x = input()
        if x == "on":
            text = text + "1"
        else:
            text = text + "0"
    return text
def change(text):
    """change"""
    num = ""
    if text[:-1] == "1111110":
        num = "0"
    elif text[:-1] == "0110000":
        num = "1"
    elif text[:-1] == "1101101":
        num = "2"
    elif text[:-1] == "1111001":
        num = "3"
    elif text[:-1] == "0110011":
        num = "4"
    elif text[:-1] == "1011011":
        num = "5"
    elif text[:-1] == "1011111":
        num = "6"
    elif text[:-1] == "1110000":
        num = "7"
    elif text[:-1] == "1111111":
        num = "8"
    elif text[:-1] == "1111011":
        num = "9"
    else:
        num = "E"
    if text[-1] == "1":
        num += "."
    return num
def main():
    """real"""
    text = ""
    all_text = ""
    text = inp()
    all_text += change(text)
    text = inp()
    all_text += change(text)
    text = inp()
    all_text += change(text)
    if all_text.count(".") > 1 or "E" in all_text:
        print("Error")
        return
    print(f"{float(all_text):.2f}")
main()
