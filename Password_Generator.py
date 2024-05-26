import random
import string
print("Note:Password should contain Uppercase Letters,Lowercase Letters,Numbers,Symbols")
length=int(input("Enter the length of the password which you want to generate:"))
if length<=8:
    print("!!Password length should be atleast 8 characters!!")
else:
    uc=int(input("Enter how many uppercase letters should be added:"))
    lc=int(input("Enter how many lowercase letters should be added:"))
    num=int(input("Enter how many numbers should be added:"))
    ss=int(input("Enter how many special symbols should be added:"))
    l=[]
    for i in range(0,uc):
        a=random.randint(65,90)
        l.append(chr(a))
    for j in range(0,lc):
        b=random.randint(97,122)
        l.append(chr(b))
    for k in range(0,num):
        c=random.randint(0,10)
        l.append(str(c))
    sp=string.punctuation
    y=list(sp)
    for j in range(0,ss):
        d=random.randint(0,len(y)-1)
        l.append(y[d])
    print("Paswword:")
    random.shuffle(l)
    k="".join(l)
    print(k)

