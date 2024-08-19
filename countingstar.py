"""Counting Star"""
def main(text):
    """count"""
    star = ""
    comet = 0
    cons = 0
    shoot = 0
    for i in text:
        star += i
        if len(star) >= 2:
            if star in ("~*", "*~"):
                comet += 1
                star = ""
            elif star in "*/":
                shoot += 1
                star = ""
            elif star in "**":
                cons  += 1
                star = ""
            else:
                star = star[-1]
    if not comet and not cons and not shoot:
        print("Tonight is a quiet night.")
    else:
        print(f"constellation: {cons}", f"comet: {comet}", f"shooting star: {shoot}", sep = "\n")
main(input())
