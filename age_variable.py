def age_variable(age):
    if age <= 0:
        print "Invalid input."
    elif age <= 17:
        print "Please consult pediatrician."
    elif age >= 18 and age <= 30:
        print "16 x weight + 545 formula"
    elif age >= 31 and age <= 60:
        print "14.2 x weight + 593 formula"
    elif age >= 61 and age <= 70:
        print "13 x weight + 567"
    elif age >= 71 and age <= 100:
        print "13.7 x weight + 481"
    else:
        print "Age range too high, please consult Doctor. "


age_variable(50)
