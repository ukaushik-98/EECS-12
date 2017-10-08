#Udit Kaushik                   #                         
#75825974                       #                   
#Summer Session 1               #
#EECS 12                        #
#Project 1 PID 54               #
#################################
def missing_angle():
    side_number = int(input("Enter number of sides: "))
    side_list = []
    for i in range(side_number-1):
        x = int(input('Enter degree {}: '.format(i+1)))
        side_list.append(x)
   
    missing_angle = (side_number - 2) * 180 - sum(side_list)
    print('The missing angle is {}.'.format(missing_angle))

missing_angle()
