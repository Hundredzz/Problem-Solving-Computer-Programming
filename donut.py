"""code"""
def main():
    """function"""
    price = int(input())
    pro_piece = int(input())
    extra_piece = int(input())
    piece_want = int(input())
    pro_price = price * pro_piece
    pro_set = pro_piece + extra_piece
    pro_time = piece_want // pro_set
    left = piece_want % pro_set
    if left >= pro_piece:
        pro_time += 1
        all_price = pro_time * pro_price
        all_piece = pro_time * pro_set
    else:
        all_price = pro_time * pro_price + left * price
        all_piece = pro_time * pro_set + left
    print(all_price, all_piece)
main()
