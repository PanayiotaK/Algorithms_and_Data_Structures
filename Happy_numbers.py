def count_ephemeral(n1,n2,k):       
    start=time.time()
    All_numbers=set()               # The seqeuence of numbers produced by q.
    cacheSet={}                     # A set contains all the numbers found and their result when raised to the kth power 
    count =0                        # Counts the epemeral numbers 
    if k==3:
        ephemeralL={778,112,1198,1189,1234,1759,787,877,121}                        #prestore values that are ephemeral with k=3 (lookup table)
        NonEphemeralL={136,244,351,27,3,72,1458,24,42,53,18,81,513,729,792}          #prestore values that are not ephemenal with k=3 (lookup table)
    elif k==2:
        ephemeralL={7, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97,129,133, 139, 167, 176, 188,192, 193,219,203,208}
        NonEphemeralL={2,4,16, 37,58,89,145,42,24,98,85,61,73,5,25}
    else:
        ephemeralL= {11231,233869,444797,44688,100,10000,12131}
        NonEphemeralL= {2,13139, 6725, 4338, 4514, 1138, 4179, 9219,16,14,434,2433,228,5729,19619,11969}
    for q in range(n1,n2):        
        All_numbers.add(q)       
        new_num=q
        str_num=q                           #the number that is going to be convertated into a string
        ephFlag = False
        while new_num!=1:
            if new_num in cacheSet:         # Checks if the result has come up before, if so, no calculations need to be done.
                new_num = cacheSet[new_num] # sets the number to it's result
            else:
                Anchor = new_num                                                 
                new_num=0                
                stringOfNum = str(str_num)    
                for num in map(int, stringOfNum):  #takes every digit raise the to the k power and creates the new number.                                 
                    new_num +=num**k
                cacheSet[Anchor] = new_num      # Adds the result into the cache set                
            if  new_num in All_numbers:         #checks if q produced the same number twice
                break
            if  new_num in ephemeralL :
                ephFlag = True              # breaks because the  number is found in the ephemeral list
                break          
            if  new_num in NonEphemeralL:
                break
            
            All_numbers.add(new_num)   
            str_num=new_num          #the number that we have to break into is digits is the new_num          
                  
        if new_num==1 or ephFlag:
            count+=1
            All_numbers.clear()         #clears the list
    return count


