import time
def count_ephemeral(n1,n2,k):       
    start=time.time()
    All_numbers=set()               # The numbers produced by q.
    cacheSet={}                     # Stores all previous results !!!!!
    count =0                        # Counts the epemeral numbers 
    if k==3:
        HappyL={778,112,1198,1189,1234,1759,787,877,121}    #prestore values that are ephemeral with k=3 (lookup table)
        UnhappyL={136,244,351,27,3,72,1458,24,42,53,18,81,513,729,792}          #prestore values that are not ephemenal with k=3 (lookup table)
    elif k==2:
        HappyL={7, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97,129,133, 139, 167, 176, 188,192, 193,219,203,208}
        UnhappyL={2,4,16, 37,58,89,145,42,24,98,85,61,73,5,25}
    else:
        HappyL= {11231,233869,444797,44688,100,10000,12131}
        UnhappyL= {2,13139, 6725, 4338, 4514, 1138, 4179, 9219,16,14,434,2433,228,5729,19619,11969}
    for q in range(n1,n2):
        All_numbers.add(q)       
        new_num=q
        str_num=q
        happyFlag = False
        while new_num!=1:
            if new_num in cacheSet:         # Checks if the result has come up before, if so, no calculations need to be done.
                new_num = cacheSet[new_num] # sets the number to it's result!!!!
            else:
                Anchor = new_num            #Kame ena print NA DIS TI ENI !!!!!             
                new_num=0                
                stringOfNum = str(str_num)    
                for num in map(int, stringOfNum):                                 
                    new_num +=num**k
                cacheSet[Anchor] = new_num # Adds the result into the cache set                
            if  new_num in All_numbers: 
                break
            if  new_num in HappyL:
                happyFlag = True    #Happy Flag= breaks because the  number is found in the HappyList
                break          
            if  new_num in UnhappyL:
                break
            
            All_numbers.add(new_num)   
            str_num=new_num             
                  
        if new_num==1 or happyFlag:
            count+=1
            All_numbers.clear()         #clears the list 
    print(time.time() - start)  
    return count


def q2test():
    """tests for the function count_ephemeral"""
    correct = True
    result = count_ephemeral(1, 10, 2)
    if result != 2:
        correct = False
        print("test failed for n1=1, n2=10, k=2; correct result is 2, result obtained was ", result)
    result = count_ephemeral(1000, 10000, 3)
    if result != 91:
        correct = False
        print("test failed for n1=1000, n2=10000, k=3; correct result is 91, result obtained was ", result)
    result = count_ephemeral(123456, 654321, 4)
    if result != 376:
        correct = False
        print("test failed for n1=123456, n2=654321, k=4; correct result is 376, result obtained was ", result)
    if correct:
        print("all tests passed")

#print( count_ephemeral(1, 10, 2))

#q2test()
