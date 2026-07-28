
print("Welcome to AI Roadmap");

name = input("Please enter your name: ")

print(f"Hello, {name}! Let us begin")

curr = input("what is your current company? ")
yoe = int(input("How many years of experience do you have? "))
DreamSalary = (input("What is your dream salary? "))

print(f"name: {name}")
print(f"company: {curr}")
print(f"years of experience: {yoe}")
print(f"dream salary: {DreamSalary}")

DOB = input("Please enter your date of birth (DD-MM-YYYY): ")

age = 2026 - int(DOB.split("-")[2])
print(f"age: {age}")