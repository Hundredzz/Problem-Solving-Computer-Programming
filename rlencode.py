"""encode"""
def main(text):
    """encode loop"""
    first = ""
    stack = ""
    answer = ""
    for value in text:
        if not first:
            first = value
        elif value != first:
            answer += str(len(stack)) + first
            first = value
            stack = ""
        stack += value
    answer += str(len(stack)) + first
    print(answer)
main(input())
