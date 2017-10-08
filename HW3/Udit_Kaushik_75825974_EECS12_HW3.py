#Udit Kaushik                   #                         
#75825974                       #                   
#Summer Session 1               #
#EECS 12                        #
#################################

def get_data():
    """
    This function reads the file and reiterates it all into a simplified list that contains the name, the SID, and the average.
    """
    infile = open('C:/UDIT/Summer Session I/EECS 12/HW3/as3.txt', 'r')
    data_list = []
    for line in infile:
        temp_list = []
        num_list = []
        line2 = line.split()
        for i in range(len(line2)):
            if i == 0 or i == 1:
                temp_list.append(line2[i])
            else:
                num_list.append(int(line2[i]))
                avg = sum(num_list)/len(num_list)
        temp_list.append(float(avg))
        data_list.append(temp_list)
    infile.close()    
    return  data_list

def quicksort(d, pivot, new_list):
    """
    This function takes the data returned by the above function and simplifies it into a pivot list and a reordered list using a recursive call.
    It also does the job of printing in the order speified.
    """
    if len(d) > 1:
        index = 0
        temp = 0
        for i in range(len(d)):
            if temp < d[i][2]:
                temp = d[i][2]
                index = i
        if temp != pivot[0]:
            pivot.append(temp)
        new_list.append(d[index])
        d.remove(d[index])
        quicksort(d, pivot, new_list)
    else:
        new_list.append(d[0])
        pivot.append(d[0][2])
        d.remove(d[0])
        print('The pivots in the quicksort funcion are: {:3.2f} {:3.2f} {:>3.2f} {:3.2f} {:3.2f}'.format(pivot[0], pivot[-1], pivot[-2], pivot[-3], pivot[-4]))
        print('The students are: ')
        for student in new_list:
            print('name:\t{:>4s}|SID:\t{:>4s}|avg:\t{:>3.2f}'.format(student[0], student[1],student[2]))
    

d = get_data()
first = d[0][2]
pivot = []
pivot.append(first)
new_list = []
quicksort(d, pivot, new_list)



