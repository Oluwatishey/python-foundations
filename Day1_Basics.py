#Program 1 - Age in days
"""
This program asks for input from user and multiplies it by 365days and prints out the result
"""
age = int(input("How old are you?: "))
new_age = age * 365
print("Your new age is: " + str(new_age) + " " + "days")


#Program 2 - Celcius to fahrenheit
"""
This program asks for input from user and converts to fahrenheit and prints out the result
"""

temp = float(input("Enter the current temperature in celcius: "))
convert = temp * 9/5 + 32
print("The Fahrenheit is now " + str(round(convert)))



# -------------------------
# Program 3: Salary Projection (5 Years)
"""
This program calculates how much a person earns in 5 years based on their monthly salary
"""
# -------------------------

salary = float(input("Enter your monthly salary: "))
yearly = salary * 12
five_year_salary  = yearly * 5
print("Your five-year salary would be: " + str(five_year_salary))



# -------------------------
# Program 4: Discount Calculator
"""
This program calculates discount of an item based on the input from the user
"""
# -------------------------

price = float(input("Enter the price of the item: "))
discount = int(input("Enter the discount of the item: "))
percent = discount/100 * price
new_price = price - percent
print("The new price of the item is: " + str(new_price))



# -------------------------
# Program 5: Grading System
"""
This program assigns grades based on exam scores
"""
# -------------------------

grade = int(input("Enter your grade marks: "))

if grade >= 85:
    print("A")
elif grade >= 65:
    print("B")
elif grade >= 55:
    print("C")
elif grade <= 40:
    print("Fail")



# -------------------------
# Program 6: BMI Calculator
"""
This program assigns grades based on exam scores
"""
# -------------------------

weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))
BMI = weight/(height*height)
print("Your BMI is: " + str(BMI))

if BMI < 18.5:
    print("You're underweight")
elif BMI < 24.9:
    print("Your weight is normal")
elif BMI < 29.9:
    print("You're overweight")
elif BMI > 30:
    print("You're obese")