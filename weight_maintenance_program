import sys

def inputAge(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("That is not a valid age. Try again.")
            continue
        else:
            return userInput

def inputGender():
    userGender = input('\nEnter your gender (M)ale or (F)emale:\t')
    userGender = userGender.lower()
    ##check gender
    isGenderCorrect = False
    while isGenderCorrect == False:
        if userGender == 'm' or userGender == 'male':
            userGender = 'm'
            isGenderCorrect = True
        elif userGender == 'f' or userGender == 'female':
            userGender = 'f'
            isGenderCorrect = True
        else:
            userGender = input('That is not a valid input. Please enter your gender (M)ale or (F)emale:\t')
            userGender = userGender.lower()
    return userGender


# MAIN PROGRAM STARTS HERE:
userAge = inputAge("Enter your age:\n")
#check age
if userAge >= 14 and userAge <= 100:#14 and 100 is inclusive this was interpreted from the spec
    isAgeCorrect = True
    userGender = inputGender()
else:
    print('You are not within the Membership age range')
    sys.exit()#ends the program if the user is not withing the membership age range


userHeight = float(input('\nEnter your height (m):\t'))
##check height
isHeightCorrect = False
while isHeightCorrect == False:
    if userHeight > 1.20 and userHeight < 2.10:
        #print('isHeightCorrect = True')
        isHeightCorrect = True
    else:
        userHeight = float(input('That is not valid. Enter your height (m):\t'))


userWeight = float(input('\nEnter your weight (kg):\t'))
##check weight
isWeightCorrect = False
while isWeightCorrect == False:
    if userWeight >= 30 and userWeight <= 250:
        isWeightCorrect = True
    else:
        userWeight = float(input('That is not valid Enter your weight (kg):\t'))


amountExercise = int(input('\nEnter the number of times you do exercise per week:\t'))
isAmountExerciseCorrect = False
while isAmountExerciseCorrect == False:
    isAmountExerciseCorrect = True
    if amountExercise < 1:
        levelOfExercise = 1.2
    elif amountExercise >= 1 and amountExercise <= 3:
        levelOfExercise = 1.375
    elif amountExercise == 4 or amountExercise == 5:
        levelOfExercise = 1.55
    elif amountExercise == 6 or amountExercise == 7:
        levelOfExercise = 1.725
    elif amountExercise >= 8:
        levelOfExercise = 1.9
    else:
        isAmountExerciseCorrect = False
        amountExercise = int(input('Enter the number of times you do exercise per week:\t'))


##check Male/Female BMI
if userGender == 'm':
    currentBMR = 88.362 + (13.397 * userWeight) + (4.799 * userHeight)
    currentBMR = round(currentBMR, 2)
else:
    currentBMR = 447.593 + (9.247 * userWeight) + (3.098 * userHeight)
    currentBMR = round(currentBMR, 2)


dailyCalorieIntake = currentBMR * levelOfExercise
currentBMI = userWeight / (userHeight * userHeight)
currentBMI = round(currentBMI,1)


##Standard BMI Categories
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



##Final Output
print('\nCurrent BMR = ', currentBMR,
      '\nCurrent BMI =', currentBMI,
      '\nTarget BMI = 22',
      '\nStandard BMI Cateogory: ', standardBMICategory,
      '\nDaily Calorie Intake =', dailyCalorieIntake)
