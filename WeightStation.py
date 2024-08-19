"""code"""
def check(weight, mid,avg):
    """function"""
    if weight < avg:
        if weight + mid <avg:
            return 1
    if weight > avg:
        if weight - mid >avg:
            return 1
    return 0
def main():
    """function"""
    count = 0
    average = float(input())
    w1 = float(input())
    w2 = float(input())
    w3 = float(input())
    sum3 = w1 +w2 +w3
    w4 = average * 4 - sum3
    sumall = sum3 + w4
    if sumall > 15000:
        print("Overweight")
    else:
        for i in (w1, w2, w3, w4):
            if check(i,average/2,average):
                print("Unbalance")
                break
            count += 1
        if count == 4:
            print(f"Pass {w4:.2f}")
main()
