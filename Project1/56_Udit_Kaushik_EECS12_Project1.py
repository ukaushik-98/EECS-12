#Udit Kaushik                   #                         
#75825974                       #                   
#Summer Session 1               #
#EECS 12                        #
#Project 1 PID 56               #
#################################

def percent_error():
    hypo_value = float(input('Enter hypothesised value: '))
    exper_value = float(input('Enter experimental value: '))
    frac_error = ((exper_value - hypo_value)/hypo_value) * 100
    print('The precent error is {:2.2f}%.'.format(frac_error))
percent_error()
