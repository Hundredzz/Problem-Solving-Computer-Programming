"""code"""
def check_win(team_a, team_b, final_set=False):
    """function"""
    win_score = 15 if final_set else 25
    if team_a >= win_score and (team_a - team_b) >= 2:
        return 1, 0
    if team_b >= win_score and (team_b - team_a) >= 2:
        return 0, 1
    return 0, 0
def main():
    """function"""
    game = input().strip()
    team_a = 0
    team_b = 0
    a_win = 0
    b_win = 0
    set_number = 1
    final_set = False
    for i in game:
        if i == "A":
            team_a += 1
        elif i == "B":
            team_b += 1
        final_set = (a_win == 2 and b_win == 2)
        a_ch, b_ch = check_win(team_a, team_b, final_set)
        if a_ch or b_ch:
            a_win += a_ch
            b_win += b_ch
            print(f"Set {set_number}: A ({team_a}) | B ({team_b})")
            team_a = 0
            team_b = 0
            set_number += 1
            if a_win == 3:
                print(f"A won {a_win}:{b_win} set")
                return
            if b_win == 3:
                print(f"B won {b_win}:{a_win} set")
                return
    if set_number <= 5:
        print(f"Set {set_number}: A ({team_a}) | B ({team_b})")
    if a_win < 3 and b_win < 3:
        print("The game has not finished yet.")
main()
