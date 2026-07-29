def main():
    monthly_salary, bonus, tax = userInput()
    net_salary, annual_salary, bonus_amount, tax_amount = calculateNetSalary(monthly_salary, bonus, tax)
    print("Your Annual Salary is: ", annual_salary)
    print("Your Bonus is: ", bonus_amount)
    print("Your Tax is: ", tax_amount)
    print("Your Net Salary after Bonus and Tax is: ", net_salary)

def userInput():
    monthly_salary = float(input("Enter your Monthly salary: "))
    bonus = int(input("Enter your Bonus percentage: "))
    tax = int(input("Enter your Tax percentage: "))
    return monthly_salary, bonus, tax

def calculateNetSalary(monthly_salary, bonus, tax):
    annual_salary = monthly_salary * 12
    bonus_amount = annual_salary * bonus / 100
    tax_amount = annual_salary * tax / 100
    net_salary = annual_salary + bonus_amount - tax_amount
    return net_salary, annual_salary, bonus_amount, tax_amount

main();