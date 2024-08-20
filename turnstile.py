'''f'''
def main():
    '''x'''
    state = False #lock
    count = 0
    while True:
        o = input()
        if o == "END":
            break
        if o == "C" and not state:
            state = True #unlock
        elif o == "P" and state :
            count+=1
            state = False
    print(count)
main()
