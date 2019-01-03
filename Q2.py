import time

def count_ephemeral(n1,n2,k):
    start=time.time()
    count=0
    All_numbers=[]
    for q in range(n1,n2):
        All_numbers.clear()
        All_numbers.append(q)
        str_number=q
        new_num=0
        found=False
        while new_num!=1 and found==False:
            sp_num=[int(i) for i in str(str_number)]
            new_num=0
            #print("to sp_num einai ", sp_num)
            for num in sp_num:
               new_num+=num**k
            if new_num in All_numbers:
                found=True
            else:                
                All_numbers.append(new_num)
                str_number=new_num
                
        if new_num==1:
            count+=1
            #print(All_numbers)
        #if found==True:
            
            #print(All_numbers)
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


# method return true if 
# n is Happy number



print(count_ephemeral(1,10000000, 4))
#q2test()
