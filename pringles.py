"""Pringles"""
def main():
    """count"""
    top = input()
    mid = input()
    bot = input()
    finger = int(input())
    new_mid = ""
    for _ in range(finger):
        new_mid += " "
    new_mid += mid[finger:]
    print(mid.count(")")-new_mid.count(")"))
    if new_mid.count(")"):
        print("There are still some left.")
    else:
        print("None.")
    print(top+"\n"+new_mid+"\n"+bot)
main()
