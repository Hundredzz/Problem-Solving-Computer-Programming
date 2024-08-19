"""code"""
def main():
    """function"""
    lesson = int(input())
    all_grade = 0
    for _ in range(lesson):
        score = float(input())
        if score>=95:
            all_grade+=4
        elif score>=90:
            all_grade+=3.5
        elif score>=85:
            all_grade+=3
        elif score>=80:
            all_grade+=2.5
        elif score>=75:
            all_grade+=2
        elif score>=70:
            all_grade+=1.5
        elif score>=65:
            all_grade+=1
        elif score>=60:
            all_grade+=0.5
        else:
            all_grade+=0
    print(f"{all_grade/lesson-0.005:.2f}")
main()
