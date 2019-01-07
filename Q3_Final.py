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
            

def testq3():
    assert good_expression("1+2+3+4")
    assert good_expression("1*2*3*4")
    assert not good_expression("(1+2+3+4)")
    assert not good_expression("(1*2*3*4)") 
    assert good_expression("(1+2)*3+4") 
    assert not good_expression("((1+2))*3+4") 
    assert good_expression("1+2*3+4") 
    assert not good_expression("1+(2*3)+4") 
    assert good_expression("1*2+3+4") 
    assert not good_expression("1*2+(3+4)")
    assert  good_expression("(1+2*3*((4+5)*6+7)+8)*9")
    assert not good_expression("((1+2))*3+4")
    assert not good_expression("1+(2*3)+4")
    assert not good_expression("1* 2+(3+4)")
    assert not good_expression("(1*2)+(2+2)")
    assert not good_expression("(1*2)*(2+2)")
    assert not good_expression("(1+2)*(2)")
    assert not good_expression("(1+2)+(2)")
    assert not good_expression("(1+2)+(2*3)")
    assert not good_expression("(1+2)*(2*2)")
    assert good_expression("(1+2)*(2+1)")
    assert not good_expression("(1+2)(2+2)")
    assert not good_expression("(1*2)+(3)")
    assert not good_expression("(1*2)*3")
    assert not good_expression("(1*2)+3")
    assert   good_expression("(1+9*2*2*((6+7)*8+9))*8")
    assert not good_expression("(1)+3")
    assert   good_expression("(((2+3)*7+2)*9+3*2)*9")
    assert not good_expression("((((1))))")
    assert not good_expression("((5+2)*(7+9))")
    assert not good_expression("(5*(7+9))")
    assert not good_expression("((7+9)*5)")
    assert not  good_expression("((1+9*2*2*((6+7)*8+9))*8)")
    assert  good_expression("(5+3)*7*2+3")
    assert not  good_expression("(2*3)+(5*2)")
    assert not good_expression("((5+3)*4)")
        
    print ("all tests passed")
    
#####################################################
def good_expression(d):    
    s=Stack()
    correct=False    
    paren_anix=0
    paren_kli=0
    count=0
    per1=False
    per2=False
    per3=False
    per4=False
    s.push(d[0])
    a=s.top()
    for i in range (0,len(d)):        
        if  d[i]=="*" and a==")":
            correct=False
            per1=True
            print("if 1")
            p=s.pop()
            while(p!="("):                
                if(p=="+"):
                    print("p= ",p)
                    correct=True                
                p=s.pop()
                a=s.top()
            s.push(d[i])
            paren_anix-=1
        print("correct1: ", correct)   
        if per1==True and correct==False:
            return False
        elif d[i]=="+" and a==")":
            correct=False
            per4=True
            print("if 1")
            p=s.pop()
            while(p!="("):                
                if(p=="+"):
                    print("p= ",p)
                    might=True            
                p=s.pop()
                a=s.top()
            c=s.pop()
            paren_anix-=1
            if c=="*" and might==True:
                correct=True
            else:
                correct=False
            s.push(d[i])
            a=s.top()
            
        if per4==True and correct==False:
            return False
          
        elif d[i]==")" and i==len(d)-1:
             correct=False
             per2=True
             print("elif 2")
             p=s.pop()             
             while(p!="("):
                print("p= ",p)
                if(p=="+"):                    
                    correct=True                    
                p=s.pop()
                a=s.top()                
             b=s.pop()
             paren_anix-=1
             print("b= ",b , "a= ",a)
             if b=="+" or s.isEmpty()==True or b==")" or paren_anix>=1 :               
                correct=False
             s.push(d[i])
             #a=s.top()
        print("correct2: ", correct, "a= ",a)  
        if per2==True and correct==False:
            return False
            
        elif d[i]==")" and a==")" :
            correct=False
            per3=True
            print("elif 3 ")
            p=s.pop()
            while(p!="("):
                print("p= ",p)
                if(p=="+"):
                    correct=True
                p=s.pop()
                a=s.top()                
            if a=="(":                
                correct=False
            paren_anix-=1
        print("correct4: ", correct, "a= ",a)          
        if per3==True and correct==False:
            return False
        
        else:                       
            s.push(d[i])
            a=s.top()
            print("else me :", d[i], "a= ", a)
            if d[i]=="(":
                paren_anix+=1
                
            if d[i]==")":
                paren_kli+=1
            count+=1    
    if count==len(d) and paren_kli==0 and paren_anix==0:
        correct=True
    print ("correct5 ",correct)
    return correct

print( good_expression("1*(5+3)*(1+3)*(9+8)"))
#testq3()

