# 25-01-2025
# first problem - calculator
# first_no=int(input('enter fist number:-'))
# second_no=int(input('enter fist number:-'))
# op_sel=input("which operation you want to use:-\n (1)Add \n (2)Subtract\n (3)Multiplication\n (4)Division\n")

# if op_sel == '1':
#     print(first_no + second_no)
    
# elif op_sel == '2':
#     print(first_no - second_no)
# elif op_sel == '3':
#     print(first_no * second_no)
# elif op_sel == '4':
#     if second_no != 0:
#         print(first_no / second_no)
# else:
#     print("invalid input")

#---------------------------------------------------------------------------------------------------------


# 26-01-2025
# a = "ashish"
# b = "kumar"
# print(a+b)
# print(len(a) , len(b))
# print(a[0:-2])
# print(b.upper())
# print(a.lower())
# print(a.capitalize())
# print(a.replace("a" , "h"))
# print(a.split("i"))
# print(a.rstrip())
# print(a.lstrip())
# print(b.find("d"))
# print(a.isalnum())
# print(a.isalpha())
# print(a.isdigit())
# print(a.islower())
# print(a.isupper())
# print(a.startswith("a"))
# print(a.swapcase())
# print(a.title())
# print(a.isprintable())
# print(a.isalpha())


#---------------------------------------------------------------------------------------------------------


# program for greeting 
# import time
# hours=int(time.strftime('%H'))
# minutes=int(time.strftime('%M'))
# seconds=int(time.strftime('%S'))
# print("Hello , current time is",hours ,"hours" ,minutes ,"minutes" ,seconds ,"seconds")
# t=int(input("enetr time:"))
# if (t>=0 and t<12):
#     print("good morning")
# elif (t >=12 and t <17):
#     print("good afternoon")
# else:
#     print("good evening")
    
#---------------------------------------------------------------------------------------------------------


# do-while
# i=0
# while(i<10):
#     print(i)  
#     i+=1
#     if(i%10==0):
#         break



#---------------------------------------------------------------------------------------------------------





# 27-01-2025
# program like KBC
# qu=[
#     "What is the capital of India?",
#     "Who is the CEO of Google?",
#     "What is the largest planet in our solar system?",
#     "Who is the founder of Facebook?",
#     "Who is the author of Harry Potter series?",
#     "What is the chemical symbol of gold?",
#     "Who is the first woman to win a Nobel Prize?",
#     "What is the largest mammal on Earth?",
#     "Who is the CEO of Amazon?",
#     "What is the smallest planet in our solar system?",
#     "Who is the founder of Microsoft?",
# ]
# an=[
#     ["New Delhi","Mumbai","Chandigarh","Banglore",1],
#     ["Mark Zuckerberg","Marie","J.K. Rowling","Sundar Pichai",4],
#     ["Jupiter","Mars","Earth","venus",1],
#     ["Mark Zuckerberg","Marie","J.K. Rowling","Sundar Pichai",1],
#     ["Faran","Raju","J.K. Rowling","Anuv",3],
#     ["Al","Au","Cu","Zn",2],
#     ["Marie Curie","Rosalind Franklin","Sally Ride","Jane Goodall",1],
#     ["Humpback whale","Fin whale","Sperm whale","Blue whale",4],
#     ["Jeff Bezos","Elon Musk","Sundar Pichai","Mark Zuckerberg",1],
#     ["Mars","Earth","venus","Mercury",3],
#     [ "Mark Zuckerberg","Sundar Pichai","Bill Gates","Jeff Bezos",3]
#     ]
# print ("Hey Guys, Welcome to KBC")
# print("You have 11 questions to win the prize money of 11 lakh")
# print("Rule for game:- \n -Total questions is 11 \n -Each questions have 4 options, one is correct")
# print(" -You have to choose one option from 4 options -If you choose correct then you awarded 1 lakh for each")
# print(" -If you choose wrong then you will be out of game")
# input("Press Enter to start playing...")
# i=0
# while(i<11):
#     print(f"\nQuestion {i + 1}: {qu[i]}")
#     for j in range(4):
#         print(f"{j + 1}. {an[i][j]}")
#     print("Enter your choice (1,2,3,4)")
#     ch=int(input())
#     if(ch<1 or ch>4):
#         print("Invalid choice")
#         break
#     else:
#         if(ch==an[i][4]):
#             print("Correct answer, you won Rs. 1 lakh")
#             i+=1
#         else:
#             print("Wrong answer, you are out of game")
#             break

# if i == 11:
#     print("\nCongratulations! You have answered all questions correctly and won total Rs. 11 lakh!")
# else:
#     print(f"\nYou won {i} lakh. Better luck next time!")
        



#---------------------------------------------------------------------------------------------------------


#28-01-2025
#program code to decode 
# print("what you want to code or decode")
# code=input("Enter your choice (code/decode): ")
# if code.lower() == "code":
#     text = input("Enter the text you want to code: ")
#     if (len(text)>=3):
#         r1="sdf"
#         r2="jkl"
#         text= r1 + text[1:] + text[0] + r2
#         print(text)
#     else:
#         print(text[::-1])
# else:
#     if code.lower()== "decode":
#         text = input("Enter the text you want to decode: ")
#         if (len(text)>=3):
#             text=text[3:-3]
#             text=text[-1] + text[:-1]
#             print(text)
#         else:
#             print(text[::-1])


#---------------------------------------------------------------------------------------------------------          
        
# program (snake water gun)
# import random 
# def check(com,user_input):
#     if com == user_input:
#         return 0

#     if (com == 2 and user_input == 0 ):
#         return -1
#     if (com == 0 and user_input == 1 ):
#         return -1
#     if (com == 1 and user_input == 2 ):
#         return -1
#     return 1
# com=random.randint(0,2)
# print("what you want to chose :- (0)snake (1)water (2)gun")
# user_input=int(input("enter your choice:"))

# score = check(com,user_input)
# print("your option is:",user_input)
# print("computer option is:",com)
# if (score == 0):
#     print("tie")
# elif (score == -1):
#     print("You lose")
# else:
#     print("you win")



#---------------------------------------------------------------------------------------------------------
# number guessing game 

# import random 
# import math
# number_to_guess = random.randint(1, 100)
# attempts =0 
# while True:
#     user=int(input("guess a number in between 1, 100:\n"))
#     attempts+=1
#     if (user>number_to_guess):
#         print("Try Again!You guessed too high")
#     elif(user<number_to_guess):
#         print("Try Again!You guessed too small")
        
#     else:
#         print(f"You guessed it right in {attempts} attempts.")
#         break

#---------------------------------------------------------------------------------------------------------


# import os
# file= os.listdir("clutter")
# i=1
# for fil in file:
#     if fil.endswith(".png"):
#         print(file) 
#         os.rename(f"clutter/{fil}",f"clutter/{i}.jpg")
#         i=i+1
   

#---------------------------------------------------------------------------------------------------------

# from pypdf import PdfWriter
# import os
# merge=PdfWriter()
# pdf=[file for file in os.listdir() if file.endswith(".pdf")]
# for i in pdf:
#     merge.append(i)
# merge.write("merged-pdf")
# merge.close()