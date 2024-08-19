"""code"""
def main(k,s,m,h):
    """converter"""
    second = divmod(k,s)
    minute = divmod(int(second[0]),m)
    hour = int(minute[0]) % h
    print(f"{hour}:{minute[1]}:{second[1]}")
main(int(input()),int(input()),int(input()),int(input()))
