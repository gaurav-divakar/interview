def flatlist(lst):
    for i in lst:
        if type(i)==list:
            flatlist(i)
        else:
            lst1.append(i)    

lst=[1, [2, 3, [4, 5, 6], [ 7, [ 8, 9, [10, 11], 12] ]]]  
lst1=[]  
flatlist(lst)
print(lst1)