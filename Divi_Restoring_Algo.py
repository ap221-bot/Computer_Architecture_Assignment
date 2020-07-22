'''Implemented by 
            18BCE008  (Krunal Agrawal)
            18BCE011  (Akshit Patel)
            18BCE040  (Karan Chauhan)
'''
#CONVERTS DECIMAL TO BINARY
def decimaltobinary(a):
    list_of_bits=[]
    while(a>0):
        num=a
        b=int(num%2)
        list_of_bits.append(b)
        num=num//2
        a=int(a/2)
    list_of_bits.reverse()
    return list_of_bits
#ADDING TWO BINARY NUMBERS
def Addition(a,b):
    addition = []
    ad = a
    c = 0
    for i in range(len(ad)-1,-1,-1):
        if(a[i]==0 and b[i]==0 and c==0):
            addition.append(0)
            c=0
        elif(a[i]==0 and b[i]==0 and c==1):
            addition.append(1)
            c=0
        elif(a[i]==0 and b[i]==1 and c==0):
            addition.append(1)
            c=0
        elif(a[i]==0 and b[i]==1 and c==1):
            addition.append(0)
            c=1
        elif(a[i]==1 and b[i]==0 and c==0):
            addition.append(1)
            c=0
        elif(a[i]==1 and b[i]==0 and c==1):
            addition.append(0)
            c=1
        elif(a[i]==1 and b[i]==1 and c==0):
            addition.append(0)
            c=1
        elif(a[i]==1 and b[i]==1 and c==1):
            addition.append(1)
            c=1
    addition.reverse()
    return addition

def leftshift(sA,sQ):
    num=sA+sQ
    a=len(num)
    for i in range(0,a-1):
        num[i]=0
        num[i]=num[i+1]
    del num[i]
    return num

def complimentofbinary(v):
    onecomplement = []
    twocomplement = []
    for a in range(0,len(v)):
        if v[a]==0:
            onecomplement.append(1)
        elif v[a]==1:
            onecomplement.append(0)

    c=1
    for b in range(len(v)-1,-1,-1):

        if(onecomplement[b]==0 and c==1):
            twocomplement.append(1)
            c=0
        elif(onecomplement[b]==1 and c==1):
            twocomplement.append(0)
            c=1
        elif(onecomplement[b]==0 and c==0):
            twocomplement.append(0)
            c=0
        elif(onecomplement[b]==1 and c==0):
            twocomplement.append(1)
            c=0
    twocomplement.reverse()
    return twocomplement

#CONVERTS BINARY TO DECIMAL
def binarytodecimal(b):
    b.reverse()
    dec=0
    for i in range(0,len(b)):
        if(b[i]==1):
            dec=dec+(2**i)
        elif(b[i]==0):
            pass
    return dec
print("->->->   DIVISION RESTORING ALGORITHM   <-<-<-")
di=int(input("Enter value of Dividend(q): "))
div=int(input("Enter value of Divisor(m): "))
q=decimaltobinary(di)
m=decimaltobinary(div)
print("Q in binary : ",*q)
if len(m) < len(q):
    diff=len(q)-len(m)
    for i in range(0,diff+1):
        m.insert(0,0)
print("M in binary : ",*m)
#ASSIGNING VALUE OF A to 0
a=[]
for i in range(0,len(m)):
    a.append(0)
print("A in binary : ",*a)

#VALUE OF -M
negetiveofM = complimentofbinary(m)
print("-M in binary : ",*negetiveofM)
print("")

n=1
#No of iterations
c=len(q)
while (c>0):
    #LEFT SHIFT A, Q
    d=leftshift(a,q)
    #TAKING THE "A" AND "Q" PART FROM THE "a"
    AA=d[0:len(a)]
    QQ=d[len(a):]
    #A<-A-M
    addaandm=Addition(AA,negetiveofM)
    b=len(QQ)+1
    if(addaandm[0]==1):
        QQ.insert(b,0)
        addaandm=Addition(addaandm,m)
    elif(addaandm[0]==0):#MSB(A)=0
        QQ.insert(b,1)
    a=addaandm
    q=QQ
    print("Step : ",n," --->  A : ",*a,"   Q :",*q,"  ")
    print("")
    n=n+1
    c=c-1
print("Quotient in binary and decimal: ",*q,",",binarytodecimal(q))
print("Remainder in binary and decimal: ",*a,",",binarytodecimal(a))