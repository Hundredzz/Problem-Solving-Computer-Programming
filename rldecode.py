"""decode"""
def main(text):
    """decode loop"""
    code = ""
    for i in text:
        code += i
        if not i.isnumeric():
            print(code[-1]*int(code[0:-1]), end="")
            code = ""
main(input())
