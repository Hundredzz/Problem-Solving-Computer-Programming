"""code"""
def hour_check(hour):
    """function"""
    if hour > 24:
        hour = 1
    return hour
def wet_check(wet):
    """function"""
    if wet >= 16:
        wet = 16
    elif wet <= 0:
        wet = 0
    else:
        pass
    return wet
def d_check(text):
    """function"""
    wet = 0
    if text == "c":
        wet = 0.50
    elif text == "n":
        wet = 1.00
    elif text == "w":
        wet = 1.50
    return wet
def n_check(text):
    """function"""
    wet = 0
    if text == "c":
        wet = 0.25
    elif text == "n":
        wet = 0.50
    elif text == "w":
        wet = 0.75
    return wet
def main():
    """function"""
    hour = int(input())
    wether = input().lower()
    lost = 0
    wet = 8
    for i in wether:
        wet = wet_check(wet)
        hour = hour_check(hour)
        night = 0<= hour <6 or 18<=hour<=24
        if not wet:
            break
        if i == "h":
            lost = 1
            break
        if i == "r":
            wet += 2.00
        elif i == "s":
            wet += 3.00
        elif night:
            wet -= n_check(i)
        else:
            wet -= d_check(i)
        hour += 1
    if lost:
        print("Lost")
    elif wet:
        print(f"Still Wet (Wet Level: {wet:.2f})")
    else:
        print("Dry")
main()
