#Udit Kaushik                   #                         
#75825974                       #                   
#Summer Session 1               #
#EECS 12                        #
#Project 1 PID 55               #
#################################

def main():
    x1 = int(input("Please enter the first X value: "))
    y1 = int(input("Please enter the first Y value: "))
    x2 = int(input("Please enter the second X value: "))
    y2 = int(input("Please enter the second X value: "))
    #Slope:
    print('The slope is', (y2 - y1 )/(x2 - x1))
    #Midpoint:
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    print('The midpoint is ({},{}).'.format(x,y))

main()
