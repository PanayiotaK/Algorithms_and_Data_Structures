def Merge(lefts,rights):
    result=[]    
    while len(lefts)>0 or len(rights)>0 :        
        if len(lefts)>0 and len(rights)>0:          #if both lists still have elements inside them        
            if lefts[0]< rights[0]:                 #and the first element on the left list is smaller than the first element of the right list             
                result.append(rights[0])            #the  final result will be append with the right element and remove it from the rights lists 
                rights.remove(rights[0])
            else:               
                result.append(lefts[0])             #else the results list will be append with the element of the left list 
                lefts.remove(lefts[0])

        elif len(lefts)>0 :                         #the right list is empty but the left list is not     
                result.extend(lefts)
                lefts.clear()
      
        else:   
            result.extend(rights)
            rights.clear()
    return result

def SelectionSort(d,n):      
    for i in range(n):
        element=d[i]        #the smallest value in the list
        pos=i               #the position of the smallest element found
        for j in range(i+1,n):            
            if d[j]<element:                
                element=d[j]
                pos=j
        temp=d[i]               #swaps the 2 elements
        d[i]=d[pos]
        d[pos]=temp  
    d.reverse()
            

def MergeSort(m):    
    if len(m)<=4:                 #if the length of the list is 4 or less than 4.The list will be sorted with Selection Sort
        SelectionSort(m,len(m))       
        return m
    middle=len(m)//2    #finds the middle of the list       
    left=[]             #the left list 
    right=[]            #the right list 
    leftsorted=[]       #the sorted left list
    rightsorted=[]      #the sorted right list 
    left=m[:middle]   
    right=m[middle:len(m)]    
    leftsorted=MergeSort(left)    
    rightsorted=MergeSort(right)    
    return Merge(leftsorted,rightsorted)
            

