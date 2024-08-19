"""key"""
def main(num):
    """decode key"""
    first_value = sum(int(i) for i in num)
    second_value = int(num[-3:]) * 10
    final_value = first_value + second_value
    if final_value < 1000:
        final_value += 1000
    print(str(final_value)[-4:])
main(input())
