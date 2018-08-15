def age_variable_male(age):
    if age <= 0:
        print "Invalid input."
    elif age <= 17:
        print "Please consult pediatrician."
    elif age >= 18 and age <= 30:
        print "MALE (16 x weight +) 545 - formula"
    elif age >= 31 and age <= 60:
        print "MALE (14.2 x weight) + 593 - formula"
    elif age >= 61 and age <= 70:
        print "MALE (13 x weight +) 567 - formula"
    elif age >= 71 and age <= 100:
        print "MALE (13.7 x weight) + 481 - formula"
    else:
        print "Age range too high, please consult Doctor. "


def age_variable_female(age):
    if age <= 0:
        print "Invalid input."
    elif age <= 17:
        print "Please consult pediatrician."
    elif age >= 18 and age <= 30:
        print "FEMALE (13.1 x weig)ht + 558 - formula"
    elif age >= 31 and age <= 60:
        print "FEMALE (9.74 x weig)ht + 694 - formula"
    elif age >= 61 and age <= 70:
        print "FEMALE (10.2 x weig)ht + 572 - formula"
    elif age >= 71 and age <= 100:
        print "FEMALE (10 x weight) + 577 - formula"
    else:
        print "Age range too high, please consult Doctor. "
