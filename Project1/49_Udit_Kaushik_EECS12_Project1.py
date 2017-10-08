#Udit Kaushik                   #                         
#75825974                       #                   
#Summer Session 1               #
#EECS 12                        #
#Project 1 PID 49               #
#################################

def interest_total():
    initial = float(input("Please enter the initial amount: "))
    interest = float(input("Please enter the interest rate (in percent): "))/100
    time = float(input("Please enter the amount of time (in months): "))
    total = initial * (1 + interest * time)
    print('Given the inital amount ${}, the interest rate {:.2f}, and  {} months, the amount accrued is ${:3.2f}'.format(initial, interest, time, total))

interest_total()
