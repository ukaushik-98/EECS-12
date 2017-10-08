def data():
    """
        This function gets the data from the user and places it into a list of strings.
        Please input integer values. When done, hit 'q'.
    """
    response = input('Please enter a value: ')
    score_list = []
    while True:
        if response != 'q':
            score_list.append(response)
            response = input('Please enter a value: ')
        elif response == 'q':
            return score_list
            break
        
def new_list(x:list) -> int:
    """
        This function places the accumulated values from the data function into a new list of integers.
    """
    new_score_list = []
    for item in x:
        new_score_list.append(int(item))
    return sum(new_score_list)/len(new_score_list)

def length_of_list(y:list) -> int:
    """
        This function gets the length of the list in which our data is stored.
    """
    return len(y)

def grade(w:int) -> str:
    """
        This function converts the average of the data inputed, which is recieved from the data function, into a letter grade.
    """
    if w >= 90:
        return 'A'
    elif 90 > w >= 80:
        return 'B'
    elif 80 > w >= 70:
        return 'C'
    elif 70 > w >= 60:
        return 'D'
    elif 60 > w:
        return 'F'

def main(z):
    """
        This is the main function. It's basically present to print out the final statement line of our function and call the other functions in the program.
    """
    a = length_of_list(z) #this line stores the output of the length_of_list function. The z varriable is the output of the data function.
    b = new_list(z) #this line stores the output of the new_list function. The z varriable is the output of the data function.
    c = grade(b) #this line stores the output of the grade function. The z varriable is the output of the new_list(z) function (stored in the varriable b).
    print("The number of scores entered is {}, the average is {:03.2f}, and the letter grade is {}.".format(a, b, c)) 
    

main(data()) #this line calls the main function and passes the data function through main.
