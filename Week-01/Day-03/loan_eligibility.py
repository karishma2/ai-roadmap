def main():
    age = int(input("Enter your Age: "))
    monthly_salary = float(input("Enter your Monthly Salary: "))
    credit_score = int(input("Enter your Credit Score: "))
    reason = checkLoanEligibility(age, monthly_salary, credit_score)
    if reason:
        print(reason)
    else:
        print("You are eligible for a loan.")


def checkLoanEligibility(age, monthly_salary, credit_score):
    if age >= 21 and monthly_salary >= 30000 and credit_score >= 700:
        return None
    elif age < 21:
        return "You are not old enough to apply for a loan."
    elif monthly_salary < 30000:
        return "Your monthly salary is too low to qualify for a loan."
    else:
        return "Your credit score is too low to qualify for a loan."

main();