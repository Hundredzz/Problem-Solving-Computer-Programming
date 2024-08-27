"""pringle"""
def main(top,mid,bot,finger):
    """function"""
    pick = mid[:finger].count(")")
    mid = (" "*finger) + mid[finger:]
    left = mid.count(")")
    print(pick)
    if left:
        print("There are still some left.")
    else:
        print("None.")
    print(top+"\n"+mid+"\n"+bot)
main(input(),input(),input(),int(input()))
