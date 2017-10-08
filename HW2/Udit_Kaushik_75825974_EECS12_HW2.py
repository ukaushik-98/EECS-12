def pnp(a, b):
    """
    This is the pass/no pass function.
    It compares the student's average to the class average.
    """
    if a >= b:  #if the student average > class average, student passes
        return('P')
    else:
        return('NP')   #if the student average < class average, student doesn't pass

def class_avg():
    """
    This function solves for the class average.
    """
    infile = open("hw2.txt", "r")   #file from which data is read
    class_avg = 0                   #file is closed in the student average function
    count = 0
    for line in infile:
        a = line.split(' ')
        if a != ['\n']: 
            for i in range(1, len(a)):
                count += 1              
                class_avg += int(a[i])
    return class_avg/count

def stdt_avg(class_avg:int):
    """
    This function solves for the student average.
    """
    infile = open("hw2.txt", "r")   #file from which data is read
    for line in infile:
        a = line.split(' ')
        stdt_list = []
        if a != ['\n']: 
            for i in a:
                stdt_list.append(i)
            print("SID", a[0], end = ' ')   #prints student ID
            stdt_total = 0
            count = 0
            for i in range(1, len(stdt_list)):
                count += 1
                stdt_total += int(a[i])
                stdt_avg = int(stdt_total/count)
                if i != len(stdt_list)-1:
                    x = "HW"+str(i)              
                    print('{} {:>3s}'.format(x, a[i]), end = ' ')   #prints all but the last HW and their scores
                else:                                               
                    b = int(a[i].strip('\n'))
                    x = "HW"+str(i)
                    pass_fail = pnp(stdt_avg, class_avg)
                    print('{} {:>3.0f} AVG {:>3.0f} Grade {:<2s}'.format(x,b,stdt_avg,pass_fail)) #prints last HW, average, and grade
    print('Class Average is', int(class_avg)) #prints class average
    infile.close()      #file closes

stdt_avg(class_avg())   #calls student average function while passing class average through it
