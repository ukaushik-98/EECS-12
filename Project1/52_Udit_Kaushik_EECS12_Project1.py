#Udit Kaushik                   #                         
#75825974                       #                   
#Summer Session 1               #
#EECS 12                        #
#Project 1 PID 52               #
#################################

def username(n ,first, last):
    print(n[2:]+last[:7]+first[:7])

user_input = str(input("Please graduation year: "))
user_first = str(input("Please enter your first name: "))
user_last = str(input("Please enter your last name: "))

username(user_input, user_first, user_last)
