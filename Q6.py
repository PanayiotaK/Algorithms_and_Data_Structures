count=0
def Merge(lefts,rights):
    result=[]
    global count
    while len(lefts)>0 or len(rights)>0 :
        #print("left length ", len(lefts))
        #print("right length ", len(rights))
        
        if len(lefts)>0 and len(rights)>0:
            count+=1
            if lefts[0]< rights[0]:
                count+=1
                result.append(rights[0])
                rights.remove(rights[0])
            else:
                count+=1
                result.append(lefts[0])
                lefts.remove(lefts[0])

        elif len(lefts)>0 :
                count+=1
                result.extend(lefts)
                lefts.clear()
      
        else:
            #if len(lefts)==0 and  len(rights)>0 :
                #print("else ")
                count+=1
                result.extend(rights)
                rights.clear()
        
        count+=1
        #print("lefts ",lefts)
        #print("result ",result)
    return result

def SelectionSort(d,n):
    global count  
    for i in range(n):
        element=d[i]
        pos=i        
        count+=1
        for j in range(i+1,n):
            count+=2
            if d[j]<element:                
                element=d[j]
                pos=j
        temp=d[i]
        d[i]=d[pos]
        d[pos]=temp       
     
    #print("d =",d)
    
    d.reverse()
            

def MergeSort(m):
    global count
    if len(m)<=4:
        SelectionSort(m,len(m))
        count+=1
        return m
    middle=len(m)//2
    left=[]
    right=[]
    leftsorted=[]
    rightsorted=[]
    left=m[:middle]
    #print("left= ", left)
    right=m[middle:len(m)]
    #print("right ",right)
    leftsorted=MergeSort(left)
    #print("leftsorted= ",leftsorted)
    rightsorted=MergeSort(right)
    #print("rightsorted= ",rightsorted)
    
    print("count ", count)
    return Merge(leftsorted,rightsorted)
            
                


print(MergeSort([7,5,9,3,6]))
