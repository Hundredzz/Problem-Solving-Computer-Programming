"""code"""
def main():
    """function"""
    text = input()
    most = float(input())
    mid = float(input())
    least = float(input())
    if most < mid:
        mid,most = most,mid
    if most < least:
        least,most = most,least
    if least > mid:
        least,mid = mid,least
    if text == "Ascend":
        print(f"{least:.2f}, {mid:.2f}, {most:.2f}")
    else:
        print(f"{most:.2f}, {mid:.2f}, {least:.2f}")
main()
