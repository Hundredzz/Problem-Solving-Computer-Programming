"""palindrome"""
def new(text):
    """func"""
    if len(text) == 5 and 14 < int(text[:2]) < 20:
        text = "20:02"
    elif len(text) == 5 and text[:2] == "23" and int(text[-2:]) >=32:
        text = "0:00"
    elif len(text) == 4 and int(text[-1]) < int(text[0]):
        if text[-1] != text[0]:
            text = text[:-1] + text[0]
    elif len(text) == 4 and int(text[-1]) >= int(text[0]):
        if int(text[-2]) < 5:
            text = text[:-2] + str(int(text[-2])+1) + text[0]
        else:
            text = str(int(text[:-3]) + 1) + ":0" + str(int(text[:-3]) + 1)[0]
    elif len(text) == 5 and int(text[:-3][::-1]) > int(text[-2:]):
        text = text[:3] + text[:2][::-1]
    else:
        text = str(int(text[:2])+1) +":"+ str(int(text[:2])+1)[::-1]
    return text
def main():
    """code"""
    time = int(input())
    text = input()
    text = new(text)
    for _ in range(time):
        print(text)
        if len(text) == 4:
            if int(text[-2]) < 5:
                text = text[:-2] + str(int(text[-2])+1) + text[-1]
            elif int(text[-2]) >= 5:
                text = str(int(text[:-3])+ 1) + ":0" + str(int(text[:text.find(":")])+ 1)[0]
        elif 14 < int(text[:2]) < 20:
            text = "20:02"
        elif text[:2] == "23":
            text = "0:00"
        else:
            text = str(int(text[:2])+1) + ":" + str(int(text[:2])+1)[::-1]
main()
