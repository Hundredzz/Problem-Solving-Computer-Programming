"""frame"""
def main(text):
    """create frame"""
    print("*"*(len(text)+2)+"\n"+f"*{text}*"+"\n"+"*"*(len(text)+2))
main(input())
