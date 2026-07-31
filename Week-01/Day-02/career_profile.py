def main():
    name, Age, currentCompany, yearsOfExperience, currentSalary, dreamSalary, dreamRole = userInput()
    displayProfile(name, Age, currentCompany, yearsOfExperience, currentSalary, dreamSalary, dreamRole) 

def userInput():
    name = input("Enter your Name: ")
    Age = int(input("Enter your Age: "))    
    currentCompany = input("Enter your Current Company: ")
    yearsOfExperience = int(input("Enter your Years of Experience: "))  
    currentSalary = float(input("Enter your Current Salary: "))
    dreamSalary = float(input("Enter your Dream Salary: "))
    dreamRole = input("Enter your Dream Role: ")
    return name, Age, currentCompany, yearsOfExperience, currentSalary, dreamSalary, dreamRole

def displayProfile(name, Age, currentCompany, yearsOfExperience, currentSalary, dreamSalary, dreamRole):
    print("\nCareer DashBoard:")
    print(f"Name: {name}")
    print(f"Age: {Age}")
    print(f"Current Company: {currentCompany}")
    print(f"Years of Experience: {yearsOfExperience}")
    print(f"Current Salary: {currentSalary}")
    print(f"Dream Salary: {dreamSalary}")
    print(f"Dream Role: {dreamRole}") 
    print(f"Salary Gap: {dreamSalary - currentSalary}")
    print(f"Need to {dreamSalary - currentSalary} to reach your goal.")
    if dreamSalary - currentSalary > 0:
        print(f"You need {dreamSalary - currentSalary} LPA more annually to reach your goal.")
    else:
        print(f"You have already reached your dream salary of {dreamSalary}.")

main();
