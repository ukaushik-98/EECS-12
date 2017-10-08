#Udit Kaushik                   #                         
#75825974                       #                   
#Summer Session 1               #
#EECS 12                        #
#Project 1 PID 53               #
#################################

def presidents():
    user_input = int(input("Please enter the number of the President: "))
    infile = open("presidents.txt", "r")
    presidents_list = infile.readlines()
    print(presidents_list[user_input-1].replace("\t", ", "))
presidents()
