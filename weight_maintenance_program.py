# WEIGHT MAINTENANCE PROGRAM

#IMPORTS
import sys

# output information to display to the user
def finalOutput(userData):
    currentBMR = userData[5]
    currentBMI = userData[7]
    standardBMICategory = userData[8]
    dailyCalorieIntake = userData[6]
    print("\nHere is you data:\n\nCurrent BMR = ", currentBMR,
      "\nCurrent BMI = ", currentBMI,
      "\nTarget BMI = 22",
      "\nStandard BMI Cateogory: ", standardBMICategory,
      "\nDaily Calorie Intake = ", dailyCalorieIntake)
    
    print("\nThanks for using the Weight Maintenance Program.\n")
    quit()

# check bmi categories
def bmiCategories(userData):
    # Standard BMI Categories
    currentBMI = userData[7]
    if currentBMI < 18.5:
        standardBMICategory = 'Underweight'
        'Normal weight'
        'Overweight'
        'Obese'
    elif currentBMI >= 18.5 and currentBMI <= 24.9:
        standardBMICategory = 'Normal weight'
    elif currentBMI >= 25 and currentBMI <= 29.9:
        standardBMICategory = 'Overweight'
    elif currentBMI > 30:
        standardBMICategory = 'Obese'
    else:
        standardBMICategory = 'cannot be calculated'
    userData.append(standardBMICategory)
    return userData

# calculate output data
def calculations(userData):
    userHeight = userData[2]
    userWeight = userData[3]
    levelOfExercise = userData[4]
    currentBMR = userData[5]

    dailyCalorieIntake = currentBMR * levelOfExercise
    userData.append(dailyCalorieIntake)

    currentBMI = userWeight / (userHeight * userHeight)
    currentBMI = round(currentBMI,1)
    userData.append(currentBMI)
    return userData

# check whether the user is female or male
def checkGender(userData):
    # extract data
    userGender = userData[1]
    userHeight = userData[2]
    userWeight = userData[3]
    # check Male/Female BMI
    if userGender == 'm':
        currentBMR = 88.362 + (13.397 * userWeight) + (4.799 * userHeight)
        currentBMR = round(currentBMR, 2)
        userData.append(currentBMR)
        return currentBMR
    else:
        currentBMR = 447.593 + (9.247 * userWeight) + (3.098 * userHeight)
        currentBMR = round(currentBMR, 2)
        userData.append(currentBMR)
        return currentBMR

# input amount of exercise function
def inputAmountExercise(userData):
    while True:
        try:
            amountExercise = int(input('\nEnter the number of times you do exercise per week:\t'))
        except ValueError:
            print ("That is not valid. Try again.")
        else:
            if amountExercise == "":
                print("You have not entered anything. Please enter an amount.")
            else:
                if amountExercise < 1:
                    levelOfExercise = 1.2
                    userData.append(levelOfExercise)
                    return userData
                elif amountExercise >= 1 and amountExercise <= 3:
                    levelOfExercise = 1.375
                    userData.append(levelOfExercise)
                    return userData
                elif amountExercise == 4 or amountExercise == 5:
                    levelOfExercise = 1.55
                    userData.append(levelOfExercise)
                    return userData
                elif amountExercise == 6 or amountExercise == 7:
                    levelOfExercise = 1.725
                    userData.append(levelOfExercise)
                    return userData
                elif amountExercise >= 8:
                    levelOfExercise = 1.9
                    userData.append(levelOfExercise)
                    return userData
                else:
                    print("Sorry that is not valid, please try again.")

# input weight function
def inputWeight(userData):
    while True:
        try:
            userWeight = float(input('\nEnter your weight (kg):\t'))
        except ValueError:
            print ("That is not a valid weight. Try again.")
        else:
            if userWeight == "":
                print("You have not entered anything. Please enter your weight (number).")
            else:    
                if userWeight >= 30 and userWeight <= 250:
                    userData.append(userWeight)
                    return userData
                else:
                    print("Sorry!")

# input height function
def inputHeight(userData):
    while True:
        try:
            userHeight = float(input('\nEnter your height (m):\t'))
        except ValueError:
            print ("That is not a valid height. Try again.")
        else:
            if userHeight == "":
                print("You have not entered anything. Please enter your height (number).")
            else:
                if userHeight > 1.20 and userHeight < 2.10:
                    userData.append(userHeight)
                    return userData
                else:
                    print("Sorry!")

# input gender function
def inputGender(userData):
    while True:
        try:
            userGender = input('\nEnter your gender (M)ale or (F)emale:\t')
            userGender = userGender.lower()
        except ValueError:
            print("Sorry your input is not valid. Please try again.")
        else:
            ##check gender
            if userGender == 'm' or userGender == 'male':
                userGender = 'm'
                userData.append(userGender)
                return userData
            elif userGender == 'f' or userGender == 'female':
                userGender = 'f'
                userData.append(userGender)
                return userData
            else:
                print('That is not a valid input. Please try again.')

# input age function
def inputAge():
    while True:
        try:
            userAge = int(input("Please enter your age:\t"))
        except ValueError:
            print("That is not a valid age. Try again.")
        else:
            #check age
            if userAge == "":
                print("You have not entered anything. Please enter a number.")
            elif userAge >= 14 and userAge <= 100:#14 and 100 is inclusive this was interpreted from the spec
                userData = [userAge]
                return userData
            else:
                print('You are not within the Membership age range')
                sys.exit()# ends the program if the user is not withing the membership age range

# welcome message function
def welcomeMessage():
    print("--------------------------------------------------")
    print("----Welcome to the Weight Maintenance Program!----")
    print("--------------------------------------------------")
    try:
        continueProgram = input("Press ENTER to continue...")
    except ValueError:
        print("Sorry that is not a valid input. Try Again.")
    else:
        if continueProgram == "":
            print("Starting Program...")
            userData = inputAge()
            userData = inputGender(userData)
            userData = inputHeight(userData)
            userData = inputWeight(userData)
            levelOfExercise = inputAmountExercise(userData)
            currentBMR = checkGender(userData)
            userData = calculations(userData)
            standardBMICategory = bmiCategories(userData)
            finalOutput(userData)
        else:
            print("Thanks for visiting. Bye!")

# MAIN CODE

welcomeMessage()
