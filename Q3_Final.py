#q3.py
#algorithms and data structures assignment 2018-19 question 3
#matthew johnson 21 november 2018

#####################################################

"""See adspractical4.py for further explanations of the usage of stacks
and queues."""

#####################################################

class Node:
    def __init__(self, data, before=None, after=None):
        self.data = data
        self.before = before
        self.after = after

########
#STACKS#
########

class Stack:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def pop(self):
        output = self.head.data
        self.head = self.head.before
        return output
    def push(self, data):
        self.head = Node(data, self.head)
    def top(self):
        return self.head.data

########
#QUEUES#
########

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def isEmpty(self):
        return self.front == None
    def dequeue(self):
        output = self.front.data
        self.front = self.front.after
        if self.front == None:
            self.rear = None
        return output
    def enqueue(self, data):
        if self.rear == None:
            self.front = Node(data)
            self.rear = self.front
        else:
            self.rear.after = Node(data, self.rear)
            self.rear = self.rear.after
    
#####################################################
 
#####################################################
def good_expression(d):    
    s=Stack()
    correct=False    
    paren_open=0
    paren_clo=0
    count=0
    might=False
    pass1=False 
    pass2=False
    pass3=False
    pass4=False
    s.push(d[0])
    a=s.top()
    for i in range (0,len(d)):        
        if  d[i]=="*" and a==")":               #after the parenthesis there is  a * sign. For the expression to be true there must be at least one + sign between the numbers in the parenthesis 
            correct=False
            pass1=True 
            p=s.pop()
            while(p!="("):          #while the closing parenthesis is not found do the following                
                if(p=="+"):
                    correct=True     #if at least one + sign is found that means the parenthesis is true           
                p=s.pop()
                a=s.top()
            s.push(d[i])            #push the sign to the stack
            paren_open-=1           #the count for opening parenthesis decreases      
         
        if pass1==True and correct==False:      #if there is a * sign before the parenthesis but inside it there isn't a + sign that means the expression is bad. 
            return False
        elif d[i]=="+" and a==")":          #if there is a + after the parenthesis. The program checks for * before the parenthesis and at least one + inside the parenthesis.
            might=False
            correct=False
            pass4=True            
            p=s.pop()
            while(p!="("):                
                if(p=="+"):                    
                    might=True            
                p=s.pop()
                a=s.top()
            c=s.pop()
            paren_open-=1
            if c=="*" and might==True:      
                correct=True
            else:
                correct=False
            s.push(d[i])
            a=s.top()
            
        if pass4==True and correct==False:   #if the parenthesis is bad(doen't contain + inside and a * outside) then the expression is also bad
            return False
          
        elif d[i]==")" and i==len(d)-1:     #if the last element is a closing parenthesis it checks if there is a + inside the parenthesis and a * before of it, to be good.
             correct=False
             pass2=True             
             p=s.pop()             
             while(p!="("):                
                if(p=="+"):         #checks for at least one + inside the parenthesis                    
                    correct=True                    
                p=s.pop()
                a=s.top()                
             b=s.pop()
             paren_open-=1             
             if b=="+" or s.isEmpty()==True or b==")" or paren_open>=1 :     #if there is a + sign before , or redundant brackets,then the expression is bad          
                correct=False
             s.push(d[i])             
       
        if pass2==True and correct==False:          #if there is a closing parenthesis but, no + sign inside and a * outside then the expression is bad
            return False
            
        elif d[i]==")" and a==")" :                 #if there are 2 closing brackets make sure that there aren't redundant 
            correct=False    
            pass3=True            
            p=s.pop()
            while(p!="("):                
                if(p=="+"):
                    correct=True
                p=s.pop()
                a=s.top()                
            if a=="(":                
                correct=False
            paren_open-=1                  
        if pass3==True and correct==False:  #if the parenthis is bad then the expression is also false 
            return False
        
        else:                               # add all the numbers and signs in the stack if none of the if statments are satisfied                    
            s.push(d[i])
            a=s.top()            
            if d[i]=="(":
                paren_open+=1
                
            if d[i]==")":
                paren_clo+=1
            count+=1    
    if count==len(d) and paren_clo==0 and paren_open==0:    #if there are no parenthesis then the expresion is always good 
        correct=True    
    return correct


