"""code"""
def main():
    """func"""
    num = input()
    state = str.maketrans("10","01")
    if not int(num.translate(state)):
        return
    print(int(num.translate(state)))
main()
