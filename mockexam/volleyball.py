"""code"""
def win_check(team_a,team_b):
    """function"""
    a_win = 0
    b_win = 0
    if team_a > team_b:
        a_win = 1
    else:
        b_win = 1
    return a_win,b_win

def main():
    """function"""
    game = input()
    team_a = 0
    team_b = 0
    g_set = 1
    b_win = 0
    a_win = 0
    a_ch = 0
    b_ch = 0
    for i in game:
        if team_b >= 25 and team_a >= 25:
            if abs(team_a - team_b) >=2:
                a_ch,b_ch = win_check(team_a,team_b)
                a_win += a_ch
                b_win += b_ch
                print(f"Set {g_set}: A ({team_a}) | B ({team_b})")
                team_a = 0
                team_b = 0
                g_set += 1
        elif (team_b >= 25 or team_a >= 25) and (team_b < 24 or team_a < 24):
            a_ch,b_ch = win_check(team_a,team_b)
            a_win += a_ch
            b_win += b_ch
            print(f"Set {g_set}: A ({team_a}) | B ({team_b})")
            team_a = 0
            team_b = 0
            g_set += 1
        if i == "A":
            team_a += 1
        else:
            team_b += 1
    print(f"Set {g_set}: A ({team_a}) | B ({team_b})")
    if team_b >= 25 and team_a >= 25:
        if abs(team_a - team_b) >= 2:
            a_ch,b_ch = win_check(team_a,team_b)
            a_win += a_ch
            b_win += b_ch
    elif (team_b >= 25 or team_a >= 25) and (team_b < 24 or team_a < 24):
        a_ch,b_ch = win_check(team_a,team_b)
        a_win += a_ch
        b_win += b_ch
    if a_win == 3:
        print(f"A won {a_win}:{b_win} set")
    elif b_win == 3:
        print(f"B won {b_win}:{a_win} set")
    else:
        if team_b >= 25 and team_a >= 25:
            if abs(team_a - team_b) >= 2:
                print(f"Set {g_set+1}: A (0) | B (0)")
        elif (team_b >= 25 or team_a >= 25) and (team_b < 24 or team_a < 24):
            print(f"Set {g_set+1}: A (0) | B (0)")
        print("The game has not finished yet.")
main()
