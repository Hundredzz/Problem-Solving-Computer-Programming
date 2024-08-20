"""saitama"""
import math
def main():
    """wid"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    a2 = math.ceil(a/int(input()))
    b2 = math.ceil(b/int(input()))
    d2 = math.ceil(d/int(input()))
    c2 = math.ceil(c/int(input()))
    most = -20000000000000000
    if a2 > most:
        most = a2
    if b2 > most:
        most = b2
    if c2 > most:
        most = c2
    if d2 > most:
        most = d2
    print(int(most))
main()
