# Hunter Pollard
# This program is used to allow people to choose different calculators for peoples fitness desires
# Here are the numeric operators and functions that couldn't fit into my program
# Divides numbers without remained (Floor Division)
# print(11 // 5)
# Prints remainder for division (Modulus)
# print(11 % 5)
# End comment (Puts a space instead of ending the line of code)
def bmi_calculator(height_in, weight_lbs):
    y = 1
    while y > 0:
        bmi = weight_lbs * 703 / height_in ** 2
        if bmi >= 18.5 and bmi <= 24.9:
            print("Congratulations, you're bmi is {:,.2f}.".format(bmi), "You're in the healthy range of BMI.")
        elif bmi < 18.5 or bmi > 24.9:
            print("You're bmi is {:,.2f}.".format(bmi), "This is an unhealthy BMI.")
        y-=1


def body_fat_percentage_calculator(Bmi, age, gender):
    for x in range (1):
        if gender == "Man":
            body_fat_percentage_man = 1.20 * Bmi + 0.23 * age - 16.2
            print("Your body fat percentage is {:,.2f}.".format(body_fat_percentage_man))
        elif gender == "Women":
            body_fat_percentage_women = 1.20 * Bmi + 0.23 * age - 5.4
            print("Your body fat percentage is {:,.2f}.".format(body_fat_percentage_women))


def calorie_tracker():
    # For Monday
    # Calorie goal variable states the amount a person wants to intake for that day
    calorie_goalM = int(input("Enter calorie intake goal, for Monday: "))
    # Calorie intook variable is the actual amount the person has intook that day
    calorie_intookM = int(input("Enter calorie intake for Monday: "))
    if calorie_goalM == calorie_intookM:
        # Multiplication comment for string operators
        print("Nice!" * 3)
        print("you have met your goal for today!")
    elif calorie_goalM > calorie_intookM:
        print("Intake more calories by:", calorie_goalM - calorie_intookM, "")
    elif calorie_goalM < calorie_intookM:
        print("Intake less calories by:", calorie_intookM - calorie_goalM, "")
    # For Tuesday
    calorie_goalT = int(input("Enter calorie intake goal for Tuesday: "))
    calorie_intookT = int(input("Enter calorie intake for Tuesday: "))
    if calorie_goalT == calorie_intookT:
        print("Nice!" * 3)
        print("you have met your goal for today!")
    elif calorie_goalT > calorie_intookT:
        # catenation comment for string operators
        print("Intake more" + "calories by:", calorie_goalT - calorie_intookT, "")
    elif calorie_goalT < calorie_intookT:
        print("Intake less calories by:", calorie_intookT - calorie_goalT, "")
    # For Wednesday
    calorie_goalW = int(input("Enter calorie intake goal for Wednesday: "))
    calorie_intookW = int(input("Enter calorie intake for Wednesday: "))
    if calorie_goalW == calorie_intookW:
        print("Nice!" * 3)
        print("you have met your goal for today!")
    elif calorie_goalW > calorie_intookW:
        print("Intake more calories by:", calorie_goalW - calorie_intookW, "")
    elif calorie_goalW < calorie_intookW:
        print("Intake less calories by:", calorie_intookW - calorie_goalW, "")
    # For Thursday
    calorie_goalTh = int(input("Enter calorie intake goal for Thursday: "))
    calorie_intookTh = int(input("Enter calorie intake for Thursday: "))
    if calorie_goalTh == calorie_intookTh:
        print("Nice!" * 3)
        print("you have met your goal for today!")
    elif calorie_goalTh > calorie_intookTh:
        print("Intake more calories by:", calorie_goalTh - calorie_intookTh, "")
    elif calorie_goalTh < calorie_intookTh:
        print("Intake less calories by:", calorie_intookTh - calorie_goalTh, "")
    # For Friday
    calorie_goalF = int(input("Enter calorie intake goal for Friday: "))
    calorie_intookF = int(input("Enter calorie intake for Friday: "))
    if calorie_goalF == calorie_intookF:
        print("Nice!" * 3)
        print("you have met your goal for today!")
    elif calorie_goalF > calorie_intookF:
        print("Intake more calories by:", calorie_goalF - calorie_intookF, "")
    elif calorie_goalF < calorie_intookF:
        print("Intake less calories by:", calorie_intookF - calorie_goalF, "")
    # For Saturday
    calorie_goalS = int(input("Enter calorie intake goal for Saturday: "))
    calorie_intookS = int(input("Enter calorie intake for Saturday: "))
    if calorie_goalS == calorie_intookS:
        print("Nice!" * 3)
        print("you have met your goal for today!")
    elif calorie_goalS > calorie_intookS:
        print("Intake more calories by:", calorie_goalS - calorie_intookS, "")
    elif calorie_goalS < calorie_intookS:
        print("Intake less calories by:", calorie_intookS - calorie_goalS, "")
    # For Sunday
    calorie_goalSu = int(input("Enter calorie intake goal for Sunday: "))
    calorie_intookSu = int(input("Enter calorie intake for Sunday: "))
    if calorie_goalSu == calorie_intookSu:
        print("Nice!" * 3)
        print("you have met your goal for today!")
    elif calorie_goalSu > calorie_intookSu:
        print("Intake more calories by:", calorie_goalSu - calorie_intookSu, "")
    elif calorie_goalSu < calorie_intookSu:
        print("Intake less calories by:", calorie_intookSu - calorie_goalSu, "")


def main():
    print("Which option would you like to see? ")
    print("BMI Calculator")
    print("Body Fat Percentage Calculator")
    print("Calorie Tracker")
    user_input = str(input("Enter option here: "))
    if user_input == "BMI Calculator":
        height_in = int(input("Please enter your height in inches: "))
        weight_lbs = int(input("Please enter your weight in pounds: "))
        bmi_calculator(height_in, weight_lbs)
    elif user_input == "Body Fat Percentage Calculator":
        gender = str(input("Enter gender here. (Women or Man): "))
        Bmi = float(input("Enter your BMI here: "))
        age = int(input("Enter your age here: "))
        if gender == "Man":
            body_fat_percentage_calculator(Bmi, age, gender)
        elif gender == "Women":
            body_fat_percentage_calculator(Bmi, age, gender)
    elif user_input == "Calorie Tracker":
        calorie_tracker()
    else:
        print("This is not a valid input. Please enter a valid option.")
        main()


main()
