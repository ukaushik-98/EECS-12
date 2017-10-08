def read_file():
    infile = open("hw2.txt", "r")
    c = 0
    stdnt_list = []
    k = 0
    class_avg = 0
    for line in infile:
        a = line.split(' ')
        if a != ['\n']:
            stdavg = 0
            stdsum = 0
            for i in range(1, len(a)):
                stid = (a[0])
                k += 1
                stdsum += int(a[i])
                c += int(a[i])
            stdavg = stdsum/(len(a)-1)

            stdnt_list.append(stid)
            stdnt_list.append(stdavg)

    class_avg = c/k

    infile.close()
    
    for i in range(len(stdnt_list)):
        if type(stdnt_list[i])== str:
            if stdnt_list[i+1] > class_avg:
                v_pass = 'Pass'
            else:
                v_pass = 'Fail'
                
            print("SID", stdnt_list[i], stdnt_list[i+1], v_pass)
    print("Class Average is", class_avg)

    
    
read_file()
