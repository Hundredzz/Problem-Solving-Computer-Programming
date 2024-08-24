"""code"""
import math
def pool_check(low,upp,num,othe):
    """function"""
    pool = 0
    if low:
        pool += 26
    if upp:
        pool += 26
    if num:
        pool += 10
    if othe:
        pool += 32
    return pool
def streng(entrophy):
    """function"""
    if entrophy < 28:
        return "Very Weak"
    if entrophy < 36:
        return "Weak"
    if entrophy < 60:
        return "Reasonable"
    if entrophy < 128:
        return "Strong"
    if entrophy >= 128:
        return "Very Strong"
def main():
    """function"""
    text = input()
    low = 0
    upp = 0
    num = 0
    othe = 0
    for i in text:
        if i.islower():
            low += 1
        elif i.isupper():
            upp += 1
        elif i.isnumeric():
            num += 1
        else:
            othe += 1
    pool = pool_check(low,upp,num,othe)
    entropy = math.floor(math.log2(pool**len(text)))
    print(entropy)
    print(streng(entropy))
main()
