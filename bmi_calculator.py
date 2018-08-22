def metricBMI(bmi):
    text = str('placeholder')
    #
    # #Get height and weight values
    # height = float(input('Please enter your height in meters: '))
    # weight = float(input('Please enter your weight in kilograms: '))
    #
    # #Square the height value
    # heightSquared = (height * height)
    #
    # #Calculate BMI
    # bmi = weight / heightSquared

    #Print BMI value
    print ('Your BMI value is ' + str(bmi))

    if bmi < 18:
        text = 'Underweight'

    elif bmi <= 24:
        text = 'Ideal'

    elif bmi <= 29:
        text = 'Overweight'

    elif bmi <= 39:
        text = 'Obese'

    elif bmi > 40:
        text = 'Extremely Obese'

    print ('This is: ' + text)

metricBMI(20)
