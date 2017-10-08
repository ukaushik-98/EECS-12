#Udit Kaushik                   #                         
#75825974                       #                   
#Summer Session 1               #
#EECS 12                        #
#Project 1 PID 51               #
#################################
def pattern(sp, a, b, c, n):
    for i in range(n):
        print(sp * i + a)
        print(sp * i + b)
        print(sp * i + c)


space = "   "
pat1 = str(input("Please enter line 1 of a pattern: "))
pat2 = str(input("Please enter line 2 of a pattern: "))
pat3 = str(input("Please enter line 3 of a pattern: "))
user_input = int(input("Please enter the number of repetitions the pattern will make: "))
pattern(space, pat1, pat2, pat3, user_input)
