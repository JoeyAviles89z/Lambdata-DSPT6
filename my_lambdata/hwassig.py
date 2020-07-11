def add(a,b): #this is a helper function
    return a+b

def averages(lst):
    '''
    :lst: list of floats or integers
    :return: average of elements in the list
    '''
    lngth = len(lst)
    total = sum(lst)
    average = total/lngth
    return average

if __name__ == '__main__':
    a = int(input("first numer:"))
    b = int(input("second number:"))
    print(f"This is the addition function return values: {add(a, b)}") #helper function is called here

    lst = [1, 2, 3, 4, 5, 6]
    print(f"This is the average of the list: {averages(lst)}")