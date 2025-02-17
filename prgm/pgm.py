# cube 
# cube=int(input("enter no"))
# n=cube*cube*cube
# print(n)


# sqr root 
# num=int(input("enter no"))
# sq=num**0.5
# print(sq)



# number check

# n=int(input("enter"))
# if n<10:
#     print("no is single digit")
# elif n>=10 and n<=99:
#     print("no is two digit")
# elif n>99 and n<999:
#     print("no is three digit")
# else:
#     print("valid option ")

# range 
# for i in range(15,21):
#     print("cube of",i,  i**3)



# altr no sqr 1 to 10 
# for i in range(1,10,2):
#     print(i**2) 

#multi

# n1=int(input("enter no"))
# n2=int(input("enter no"))
# p=0
# c=n1
# while c> 0:
#     c=c-1
#     p=p+n2
#     print(p)

# done
# total=0
# n=input("enter no or done")
# while n != 'done':
#     num=int(n)
#     total= total+ num 
#     n=input("enter no or done:")
#     print("sum is ",total)  



#table

# for i in range(1,10):
#     for j in range (1,10):
#         print('' ,i*j,'',end='')
#         print()


#case
# line=input("enter")
# lowercount=uppercount=0
# digitcount=alphacount=0
# for i in line:
#     if i.islower():
#         lowercount+=1
#     elif i.isupper():
#         uppercount+=1
#     elif i.isdigit():
#         digitcount+=1
#     if i.isalpha():
#         alphacount+=1
# print(uppercount)
# print(lowercount)
# print(digitcount)
# print(alphacount)

# d1= {5:"num",\
#     "a" : "string",\
#     (1,2) : "tuple"}
# d2={ 4 : "num" , "b" : "string"
# }
# d2.update(d1)
# print(d2)


# competition 
# n=input("how many students:")
# win={}
# for i in range(int(n)):
#     key=input("enter name:")
#     value=input("no of comp won:")
#     win[key]=value
#     print(win)

#addition of list  
# l1=['a','b','c']
# l2=['h','i','j']
# l3=['0','1','2']
# l1.append(l2)
# l1.insert(0,l3)
# print(l1)

# individual addition of list
# l1=['a','b','c']
# l2=['h','i','j']
# l3=['0','1','2']
# l3.extend(l1)
# l3.extend(l2)
# print(l3)


# def cal(n1,n2):
#     return n1+n2
# n1=int(input("enter no"))
# n2=int(input("enter no"))
# print(cal(n1,n2))  

# def interest(pri,time=2 ,rate=0.10):
#     return pri*time*rate
# print(interest(10000))   #default value of time and rate is 2 and


# print("*".join('hello'))
# print("".join(['h','e','l','l','o']))
# print("##".join({"trail","hello"}))
# print("hey hello bro".split())

# import random 
# print(random.randint(2 ,34))
# print(random.uniform(2 ,34))
# print(random.randrange(2,34,3))


# import string
# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)  #!\"#$%&'()*+,-./:;<=>
# print(string.printable)  #all printable ascii characters
# print(string.ascii_lowercase)  #all lowercase ascii letters
# print(string.ascii_uppercase)  #all uppercase ascii letters
# print(string.hexdigits)  #all hex digits

# import pickle
# emp1={'empo': "1212" , 'sqd' : "23323" ,"sdds" : "23243"}
# emp2={'empo': "1212" , 'sqd' : "23323" ,"sdds" : "23243"}
# emp=open('st.dat','wb')
# pickle.dump(emp1,emp)   
# pickle.dump(emp2,emp)
# print("successful")
# emp.close()  #close the file object

# import csv
# stureader-=csv.reader(fh)
# stureader=csv.reader(fh,delimiter = '|')



# import tkinter
# wind=tkinter.Tk()
# tkinter.Button(wind,text='Press Me', command=wind.quit).pack()
# wind.mainloop()

# import tkinter
# def wquit():
#     print('Hello, getting out of here')
# root=tkinter.Tk()
# widgt1=tkinter.Label(root,text='Hello there')
# widgt1.pack()
# widgt2=tkinter.Button(root,text=' Click to quit',command=wquit)
# widgt2.pack()
# root.mainloop()  #starts the event loop of the application

# n=int(input("enter a no"))
# fac=1
# for i in range(1,n+1):
#     fac=fac*i
# print(fac)


# def si(p,r,t):
    
#     return (p*r*t)/100
# p=int(input("enter the principal amount"))
# r=int(input("enter the rate of interest"))
# t=int(input("enter the time"))
# simple_interest = si(p, r, t)
# print(f"Simple Interest = {simple_interest}")



