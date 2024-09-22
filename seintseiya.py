"""code"""
import math
def main():
    """function"""
    time = int(input())
    maxi = int(input())
    set1 = 165 *2 +1
    starp_time = maxi//set1
    sase = maxi % set1
    starp_sase = math.ceil(sase/165)
    allstarp = starp_time* 6 + starp_sase * 2
    timeleft = 0
    if time > allstarp:
        timeleft = time - allstarp - 1
    elif time < allstarp:
        timeleft = time // 6
        time = time % 6
        time = time //2
        print(timeleft * set1 + time * 165)
        return
    print(starp_time * set1 + starp_sase * 165 + timeleft*12)
main()
