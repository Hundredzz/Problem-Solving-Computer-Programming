"""PongYa"""
def main():
    """PongYa"""
    num = int(input())
    if not num % 3 or num % 10 == 3:
        print("PONG")
    else:
        print(num)
main()
