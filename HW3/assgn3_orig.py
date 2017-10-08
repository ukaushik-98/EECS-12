def get_data():
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
        temp_list.append(int(avg))
        data_list.append(temp_list)
        
    return  data_list

def quicksort(d, count, pivot):
    less = []
    equal = []
    greater = []
    equal.append(d[0])
    
    for i in range(1, len(d)):
        #pivot = d[i][2]
        #print(pivot)
        
        if d[i][2] > pivot:
            greater.append(d[i])  
        elif d[i][2] < pivot:
            less.append(d[i])
        else:
            equal.append(d[i])

    count += 1
    d = less + equal + greater
    
    pivot=d[0][2]
    quicksort(d, count, pivot)

    if 
    print(d)
    print(count)
    
    #for i in range(len(d)-1):
    #    if d[i] > d[i+1]:
            #count += 1
     #       quicksort(d, count, pivot_count)
    #    else:
     #       break
    #for student in d:
    #    print('name:\t{:>4s}|SID:\t{:>4s}|avg:\t{:>2d}'.format(student[0], student[1], student[2] ))
    #print(pivot_count)
    #print(d)
    #print(pivot_count)
            
def print_list():
    for student in d:
        print(pivot_count)
        print('name:\t{:>4s}|SID:\t{:>4s}|avg:\t{:>2d}'.format(student[0], student[1], student[2] ))

pivot_count = []
count = 0 
d1=get_data()
pivot=d1[0][2]
print(d1)
quicksort(d1, count, pivot)



