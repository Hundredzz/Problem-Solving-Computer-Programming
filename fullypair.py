"""fully pair"""
def main():
    """fullypair"""
    pair = input()
    sase = ""
    for i in pair:
        if pair.count(i) %2 and i not in sase:
            sase+=i
    if sase:
        print(sase)
    else:
        print("fully paired")
main()
