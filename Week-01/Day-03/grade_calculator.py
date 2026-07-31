def main():
    marks = input("Enter your marks separated by space: "  )
    calculateGrade(marks)

def calculateGrade(marks):
    marks_list = [int(mark) for mark in marks.split()]
    average_marks = sum(marks_list) / len(marks_list)
    
    if average_marks >= 90:
        grade = 'A'
    elif average_marks >= 80:
        grade = 'B'
    elif average_marks >= 70:
        grade = 'C'
    elif average_marks >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    print(f"Average Marks: {average_marks:.2f}")
    print(f"Grade: {grade}")

main();