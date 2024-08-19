'''f'''
def main():
    '''g'''
    bank = float(input())
    wallet = float(input())
    e = 0
    try:
        while True:
            o = input()
            if o == 'end':
                break
            if wallet < float(o[2:]) and 'D' in o:
                e+=1
                continue
            if bank < float(o[2:]) and 'W' in o:
                e+=1
                continue
            if e == 3:
                continue
            if "D" in o:
                bank+=float(o[2:])
                wallet-=float(o[2:])
            elif "W" in o:
                bank-=float(o[2:])
                wallet+=float(o[2:])
            e = 0
        print(f'{bank:.2f}')
        print(f'{wallet:.2f}')
    except EOFError:
        print(f'{bank:.2f}')
        print(f'{wallet:.2f}')
main()
