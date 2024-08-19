"""FOR!F-BALL"""
def main(action):
    "ball position"
    position = 1
    for i in action:
        if i == "A":
            if position == 1:
                position = 2
            elif position == 2:
                position = 1
        if i == "B":
            if position == 2:
                position = 3
            elif position == 3:
                position = 2
        if i == "C":
            if position == 1:
                position = 3
            elif position == 3:
                position = 1
    print(position)
main(input())
