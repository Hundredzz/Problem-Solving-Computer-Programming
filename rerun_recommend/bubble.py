"""bubble"""
def main(race):
    """function"""
    num = 0
    jump = 0
    distance = 0
    lose = 0
    skip = 0
    for i in race:
        num += 1
        if skip>0:
            skip -= 1
            continue
        if i in ("^","o"):
            if race[num] == " ":
                lose = 1
                distance = len(race)-num
                break
            jump+=1
        elif i == "O":
            if "|" in race[num:num+3]:
                jump += 1
                break
            if "O" in race[num:num+3] or "o" in race[num:num+3]:
                new = race[num:num+3]
                jump+=1
                skip = new.rfind("O")
                if skip < 0:
                    skip = new.rfind("o")
            else:
                lose = 1
                distance = len(race)-num
                break
    if lose:
        print("IMPOSSIBLE")
        print(distance)
        return
    print("POSSIBLE")
    print(jump)
main(input())
