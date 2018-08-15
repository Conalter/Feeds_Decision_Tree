def gender_variable(gender):
    if gender == "male":
        return m_procedure()
    elif gender == "female":
        return f_procedure()
    else:
        print "Please state gender."

def m_procedure():
    print "this is the energy requirements for a male patient"

def f_procedure():
    print "this is the energy requirements for a female patient"


        # def fib(n):
        #     result = []
        #     a, b = 0, 1
        #     while a < n:
        #         result.append(a)
        #         a, b = b, a+b
        #         print result
        #
        # f100 = fib(100)
        # f100
