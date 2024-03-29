def hash_quadratic(d):
    #count= the number of elements in the table. If count>19 the table is full 
    count=0
    table=["-"]*19         #initialise a table of size 19 with '-' in all the possitions 
    for k in d:
        p=0               #p= the initial possition  found in the hash table 
        prev_p=0
        addition=1        #the variable that increases if the found possition in the table is occupied 
        i=(6*k+3)%19
        p=i
        count+=1        
        if count>19:
            return table
        while(table[i] != '-' ):            #while there is collision  do:
            prev_p=i
            i=(p+(addition**2))% 19         #calculate the new position
            if(prev_p==i ):                 # if the previus possition  == to the new possition that means the
                                            #possition will loop back to the same possitions of the hash table  and the number will not enter the table. 
                count-=1
                break
            addition+=1                      
        if(prev_p==i and prev_p!=0):      # the number is not going to be placed in the hash table so we continue to the next number  
            continue        
        table[i]=k     
    
    return table



def hash_double(d):    
    count=0                 #counts how many numbers are entered in the hash table 
    table=['-']*19          #initialise table of size 19
    for k in d:
        addition=0
        j=1
        i=(6*k+3) % 19
        p=i
        count+=1
        if count>19:                #if count  greater than 19 that means the hash table is full 
            return table
        while(table[i] != '-'):     #if there is collision do the following statments
            addition=j*(11-(k%11))
            i=(p+addition)% 19
            j+=1
       
        table[i]=k                  #place the number to the position found                
        
    return table


def test_hq():
    assert hash_quadratic([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]) == [9, 6, 3, 19, 16, 13, 10, 7, 4, 1, 17, 14, 11, 8, 5, 2, 18, 15, 12]
    assert hash_quadratic([19,38,57,76,95,114,133,152,171,190]) == [95, 133, '-', 19, 38, '-', '-', 57, 190, 114, 171, '-', 76, '-', 152, '-', '-', '-', '-']
    assert hash_quadratic([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79]) == [47, 71, 3, 19, 43, 13, 29, 7, 23, 61, 17, 41, 11, 59, 5, 2, 37, 53, 31]
    print ("all tests passed")


def test_dh():
    assert hash_double([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]) == [9, 6, 3, 19, 16, 13, 10, 7, 4, 1, 17, 14, 11, 8, 5, 2, 18, 15, 12]
    assert hash_double([19,38,57,76,95,114,133,152,171,190,209,228,247,266,285,304,323,342,361]) == [304, 361, 266, 19, 76, 152, 228, 95, 171, 38, 114, 190, 57, 133, 209, 247, 285, 323, 342]
    assert hash_double([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79]) == [47, 67, 3, 19, 53, 13, 29, 7, 23, 59, 17, 41, 11, 61, 5, 2, 37, 43, 31]
    print ("all tests passed")




