 
def ReverseList(lst): 
    for element in lst:
        if type(element) is list:
            ReverseList(element)
    lst.reverse() 
    return lst 
      
lst = [[1, 2], [3, 4], [5, 6, 7]] 
print(ReverseList(lst))
 