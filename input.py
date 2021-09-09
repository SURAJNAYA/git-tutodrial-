# name=input("type your name")
# print ("hello" + name)
# age= input("what is your age ?")
# # print("your age is",age) 
# number_first = int(input("enter first number"))
# number_sec = int(input("enter second number"))
# total= number_first + number_sec
# print("totle is" + str(total))
# print(f"totle number {total}  ")  

#2 -*****************----******************-----------***************************-----------*******************---------*************----**********

# num1=int(input("enter first number "))
# num2=int(input("enter second number"))
# num3=int(input("enter there number"))

# average=num1+num2+ num3 //3
# print("average is",average )
# num1,num2,num3= input("enter three number").split(",") # seprited by coma ','
# sum=int(num1)+int(num2)+int(num3)
# print(sum)
# print(f"average is : { (int(num1) + int(num2) + int(num3)) /3}")

# 3***********-----************************-----------**************************-------------******************-----------*******************************

#  dictionary is nothing key velue pairs

# d1 = {"suraj":{"L":"senvich","B":"megge","D":"fesh"},"mohit":{"L":"pizaa","B":"gobi","D":"Bhindi"},
#  "mother":{"L":"eig","B":"fesh","D":"chaken"},"papa":"leadyfinger"}
# d1["lk"]="junkfood"
# print(d1)
# del d1 ["lk"]
# print(d1)  
# d1.update({"radhe":"coffe"})
# print (d1)
# print (d1.keys())
# print (d1.items())

# 4 *****************----------***********---------*********************-----------**************---------************----------*********************************

# print ( " what is your age ")
# age = int (input ())
# if age < 18 = 20:
#     print("you can't drive ")

# elif age== 18:
#     print("we will thing about it ")

# else:
#     print ("You Can Drrive ")
 
# a=int(input("enter your age"))
# if a>18 and a<100:
#     print("YOU CAN DRIVE  ")
#     print("\U0001F600	")
#     print("\U0001F61A")
# elif a==18:
#     print("WE CANNOT DECIDE WETHER YOU ARE ELIGIBLE FOR DRIVING OR NOT")
#     print("\U0001F644")
# elif a<18:
#     print("Legeally,YOU ARE NOT AUTHORIZED TO BE A DRIVER")
#     print("\U0001F612")
# else:
#     print("Illogical age")
#     print("\U0001F635  \U0001F4AB	")

# 5 *****************------********************----------*****************-----------***************-----------*****************-----------********



# faulty calculater

# 45*3=55,56+9=77 ,56/6=4


# 6 ***********---------*************-----------****************---------****************************-------************----**********
# experiment

# print ("enter your firts numer")
# num1=int(input())
# print ("enter your second number")
# num2=int(input())
# print("choose your opreation\ n1 adition \ n2 supptraction and n3 multiplication ")
# choice=int(input())
# if num1==56 and num2==9 and choice==1:
#     print("The Result is", int(77))
# elif num1==56 and num2==6 and choice==2:
#     print("The Reselt is", int(4) )
# elif num1==45 and num2==5 and choice==3:
#     print( "The Rseult is", int(555))

# elif choice==1:
#     print("Thr  sum  of the number is", num1+num2)
# elif choice==2:
#     print( "The suptraction of the number is", num1/num2) 
# else:
#     print( "The multiplication is", num1 * num2 )

# 7 ********************-------------*************----------**************----****************---------****************-------------******************------------******


# list3 = [ ["suraj","piza"],["sonu","buger"],["sonam","magge"]]
# for item,deaner in list3 :
#    print(item,";Lunch Food Name is",deaner)

# 8 *************************************loop statment***************************************************************************

# a=int(input("enter a number "))
# while a<100:
#     print(a)
#     a=a+1
# print("condition folse")

# The Breck Statment

# a=int(input("enter a number "))
# while a<100:
#     if (a==50):
#         break
#     print(a)
#     a=a+1
# print("condition folse")



# while(True):
#     ab=int(input("enter a number \n"))
#     if ab>100:
#         print("congrtulation you are enter grater then 100\n")
#         break
#     else:
#             print("try agane\n")
#             continue

# 9 ****************-------******************-----***********------********************-----**************------------**************

# n=18
# number_of_guesses=1
# print("Number of guesses is limited to only 9 times: ")
# while (number_of_guesses<=9):
#     guess_number = int(input("Guess the number :\n"))
#     if guess_number<18:
#         print("you enter less number please input greater number.\n")
#     elif guess_number>18:
#         print("you enter greater number please input smaller number.\n ")
#     else:
#         print("you won\n")
#         print(number_of_guesses,"no.of guesses he took to finish.")
#         break
#     print(9-number_of_guesses,"no. of guesses left")
#     number_of_guesses = number_of_guesses + 1

# if(number_of_guesses>9):
#     print("Game Over")

# 10 ************************-----------------**************************----------------***************************----------------**************-------------****************------------*******


# Operators In Pythons
# 1 Arithmetic Operators
# 2 Assignment Operators
# 3 Comparison Operators
# 4 Logical Operators
# 5 Identity Operators
# 6 Membership Operators
# 7 Bitwise Operators

# Arithmetic Operators
# print("5 + 6 is ", 5+6)
# print("5 - 6 is ", 5-6)
# print("5 * 6 is ", 5*6)
# print("5 / 6 is ", 5/6)
# print("5 ** 3 is ", 5**3)
# print("5 % 5 is ", 5%5)
# print("15 // 6 is ", 15//6)

# Assignment Operators
# print("Assignment Operators")
# x = 5
# print(x)
# s= x/7# x = x%7
# print(s)

# Comparison Operators
# from typing_extensions import Concatenate


# i = 5


# Logical Operators
# a = True
# b = False

# Identity Operators
# print(5 is  5)

# Membership Operators
# list = [3, 3,2, 2,39, 33, 35,32]
# print(3 not in list)

# Bitwise Operators
# 0 - 00
# 1 - 01
# 2 - 10
# 3 - 11

# 1print(0 & 2)
# print(0 | 3)

# 11 **********************------------**********--------------******************-----------------************------------*************--------------********************------------*************---------********************--------------*


# a=int(input("enter number a\n"))
# b=int(input("enter number b \n"))
# print("B A se bada he bhai") if a<b else print("A B se bada hei bhai")

# 12 **************------*************---------*************-------------**************------------***************----------****************----*


# def function1 (a,b):
#     """The Function whicle will calculate sum  of two number(this is a docstringty,hjmh`) """
#     print(" Sum Number is ",a+b)
# function1(1,9)
# print(function1.__doc__)


# 13 ******------------------***********************-----------------*****************---------------***************-------------**********


# def function2 (num1,num2):
#     """The Function whicle will calculate average of two number""" 
#     avrage= (num1+num2)/2
#     print(avrage)
#     return avrage
    
# # v=function2(12,6 )
# num1= int(input("enter first number"))
# num2=int(input("enter a second number "))
# v = function2(num1,num2)
# print(v)
# print(function2.__doc__)


# 14 ****************--------------***************************-------------------------********************************-----------------********------------***************-*


# # try except handling

# print("enter a num1")
# num1=input()
# print("enter a num2")
# num2=input()
# try:
#     print("sum of two number is ",
#     int(num1)+int(num2))

# except Exception as e:
#     print (e)

# print("This line is very importent")


# 15 *************************-------------------***********************------------------***************************------------*******************--------------****************----------





# Basde on File handling 

"""
# "r":-  Open File is Reading Mode
# "w":-m Open File is Write Mode
# "x":- Creates File if Not Exists
# "a":- Add More Contant to a File 
# "t":-Open File For text Mode
# "b":-Open File For Binary Mode
# "+":-Open File For Read and Wride Mode
"""
# f= open("F:/nayak/exempale.py ","r")
# Content = f.read()#line by line print
# for line in f:
#     print(line)
# f.close()


# f= open("F:/nayak/exempale.py ","r")
# contant=f.readline() # only file print 
# print(contant)
# f.close()

# f=open("F:/nayak/exempale.py","r")
# contant=(f.readline())# only one Line print in this stat mant
# print(contant)
# f.close()


# f=open("F:/nayak/exempale.py","r")
# contant=(f.readline())# All Line print in row line  
# print(contant)
# f.close()


# f = open("surajn.txt","a")
# a=f.write("suraj is good boy and locking is outstanding \n")
# print(a)
# f.close()


# Handle read and write both 

# def lock(k):
#     if k==1:
#         a=input("\n+Type hear ")
#         with open("surajn.txt","a") as op:
#             op.write(str(a))
#             print("successfully written")
# def retrive(k):
#     if k==2:
#         with open("surajn.txt ") as op:
#             for i in op:
#                 print (i,end=" ") 
# a=int(input("YOU Enter 1 for lock 2 for recived  "))
# if a == 1:
#     b=int(input("Enter 1 for text "))
#     lock(b)
# else:
#     b=int(input(" 2 for recived "))
#     retrive(b)
# 16 ******---------***************----------***********---------*****************------------************----------****************-----------*************------------****************-------*************-----------****************-------------*


# print ("star pattern")

# print("pattern printing")
# n=int(input("enter a  number in star partan "))
# boolean=input("true (1) or false(0)")
# if boolean=="1":
#     for i in range(1,n+1):
#         print("*" " "*i)
# if boolean=="0":    
#     for i in range(n,0,-1):
#         print("*"*i)
#     for i in range(n+1):
#             print("*" " "*i)

# 17 ******************--------*****-----------************-----------************----------************-----*************----------*************-----------*******---------********-------------*****-------------*********************------------


# globle variable

# l=15 # global variable
# def function1(n):
#     # l=5    #Local
#     m=10   #Local
#     global l
#     l=l+50
#     print(l,m)
#     print(n,"\nSuraj NaYAK Raghuvanshi")
# function1("My Name Is")

# 18 **************---------*************-------*************----------*****************------------****************----------*************------------***************------------************-------------***************------------*****************---


# x = 89
# def harry():
#     x = 20
#     def rohan():
#         global x
#         x = 88
#     print("before calling rohan()", x)
#     rohan()
#     print("after calling rohan()", x)

# harry()
# print(x)

# x = 55
# def suraj():
#     x = 15
#     def rohan():
#         global x
#         x = 90
#     print("suraj nayak",x)
#     rohan()
#     print("nayak suraj",x)

# suraj()
# print(x)

# 19 **************************--------------------*******************--------------*************-------------*************------------**************-----------*************------------******

#  factorial 
# def factorial(n):
#     fac=1
#     for i in range(n):
#         fac = fac*(i+1)
#     return fac

# number = int(input("Enter The Number"))
# print(factorial(number))


# def factorial_recursive(n):
#     if n == 1:
#         return 1

#     else:
#         return n*factorial_recursive(n-1)
# number = int(input("Enter The Number"))
# print("factorial using iterative methord",factorial_recursive(number))

# 20 **********************---------*******************-----------*************------------*************--------------*************-------------*************----------*************--------------*************


# 
# Helth Managemant system


# import datetime
# def gettime():
#     return datetime.datetime.now()
# def take(k):
#     if k==1:
#         c=int(input("enter 1 for excersise and 2 for food"))
#         if(c==1):
#             value=input("type here\n")
#             with open("harry-ex.txt","a") as op:
#                op.write(str([str(gettime())])+": "+value+"\n")
#             print("successfully written")
#         elif(c==2):
#             value = input("type here\n")
#             with open("harry-food.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#     elif(k==2):
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if (c == 1):
#             value = input("type here\n")
#             with open("rohan-ex.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#         elif (c == 2):
#             value = input("type here\n")
#             with open("rohan-food.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#     elif(k==3):
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if (c == 1):
#             value = input("type here\n")
#             with open("hammad-ex.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#         elif (c == 2):
#             value = input("type here\n")
#             with open("hammad-food.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#     else:
#         print("plz enter valid input (1(harry),2(rohan),3(hammad)")
# def retrieve(k):
#     if k==1:
#         c=int(input("enter 1 for excersise and 2 for food"))
#         if(c==1):
#             with open("harry-ex.txt") as op:
#                 for i in op:
#                     print(i,end=" ")
#         elif(c==2):
#             with open("harry-food.txt") as op:
#                 for i in op:
#                     print(i, end=" ")
#     elif(k==2):
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if (c == 1):
#             with open("rohan-ex.txt") as op:
#                 for i in op:
#                     print(i, end=" ")
#         elif (c == 2):
#             with open("rohan-food.txt") as op:
#                 for i in op:
#                     print(i, end=" ")
#     elif(k==3):
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if (c == 1):
         
#             with open("hammad-ex.txt") as op:
#                 for i in op:
#                     print(i, end=" ")
#         elif (c == 2):
#             with open("hammad-food.txt") as op:
#                 for i in op:
#                     print(i, end=" ")
#     else:
#         print("plz enter valid input (harry,rohan,hammad)")
# print("health management system: ")
# a=int(input("press 1 for lock the value and 2 for retrieve "))

# if a==1:
#     b = int(input("press 1 for harry 2 for rohan 3 for hammad "))
#     take(b)
# else:
#     b = int(input("press 1 for harry 2 for rohan 3 for hammad "))
#     retrieve(b)



# import datetime 
# def gettime():
#     return datetime.datetime.now()
# def take(k):
#     if k==1:
#         c = int(input("Enter 1 for exersise and 2 for food"))
#         if (c==1):
#             value=input("type her\n")
#             with open ("suraj_ex.txt","a") as op:
#                 op.write(str([str(gettime())])+":"+ value +"\n")
#             print(" successfully writen")
#         elif (c==2):
#             value=input("type her")
#             with open ("suraj_food.txt","a") as op:
#                 op.write (str([str (gettime())]) + ":"+ value + "\n")
#             print("successfully writen")
#     elif k==2:
#         c = int(input("Enter 1 for exersise and 2 for food"))
        
#         if (c==1):
#             value=input("type her\n")
#             with open ("munni_ex.txt","a") as op:
#                 op.write(str([str(gettime())])+":"+ value +"\n")
#             print(" successfully writen")
#         elif (c==2):
#             value=input("type her")
#             with open ("munni_food.txt","a") as op:
#                 op.write (str([str (gettime())]) + ":"+ value + "\n")
#             print("successfully writen")
#     else:
#         print("Plz enter veled input(suraj,munni)")
# def retrieve(k):
#     if k==1:        
#         c = int(input("Enter 1 for exersise and 2 for food"))
#         if (c==1):
#             with open("suraj_ex.txt") as op:
#                 for i in op:
#                     print(i,end=" ")
#         elif (c==2):
#             with open("suraj_food.txt") as op:
#                 for i in op:
#                     print(i,end =" ")
#     if k==2:        
#         c = int(input("Enter 1 for exersise and 2 for food"))
#         if (c==1):
#             with open("munni_ex.txt") as op:
#                 for i in op:
#                     print(i,end="")
#         elif (c==2):
#             with open("munni_food.txt") as op:
#                 for i in op:
#                     print(i,end ="")
#     else:
#         print("plze valed input (suraj, munni)")
# print("helth managemant system")
# a=int(input("press 1 for lock the value and 2 for retrieve  "))
        
# if a ==1:
#     b=int(input("Enter press 1 for suraj and 2 for munni"))
#     take(b)
# else:
#     b = int(input("press 1 for suraj 2 for munni "))
#     retrieve(b)

# 23 ******************-----------*******************----------***********************-------------********************----------------**********************------------************************---------------************************-----------------*************************----------------------********-


# #  Built In Modules

# import random
# random_number= random.randint(0,10)
# print(random_number)
# print("and the name is",__name__)
# if __name__== '__main__':
#     list = ["SUB","sub","UTV","UTV Action","Star Gold"]
# a= "and".join (list)
# choice=random.choice(list)
# print(choice)

# 24 **************--------***********************------------**********************----------***************-------------*********************---------------************************-----

# Fibonacci numbers module
# series is Forved order

# def fib (n):
#     a = 0
#     b = 1
#     print(a)
#     print(b)
#     for i in range (2,n):
#         c= a+ b
#         a = b
#         b = c
#         print (b)
                
# a=int(input("enter a fibo number "))
# fib(a)

# 25 ***********---------**************---------**************-------***************------------**********************------------********************-------------*********************------------*********************


#  Program to print Fibonacci 
# series in reverse order 

# def fibreverse(n):
#     a=[0]*n
#     a[0]=0
#     a[1]=1

#     for i in range(2,n):
#         a[i] = a[i-2]+a[i-1]
#     for i in  range(n-1, -1, -1):
#         print(a[i] ,end= "  ")
# n=int(input("Ednter A Fibonacci Number"))
# fibreverse(n)


# 26######################## *args / **kwargs in python###########################################################

# def funargs(*suraj):
#     for item in suraj:      
#         print(item)
# Grocery=["Dio","Solt","Asafoetida"]
# funargs(*Grocery)
   
# def fun(*suraj):
#     print(n)
#     for item in suraj:
#         print(item)
# n="This is a Monthily Grocery Items "
# grocery_Items=["Rice","Cheni","Daal","Fennel","Cumin","red Chilli"]
# fun(*grocery_Items)


# 27 ########################################## use of import ##############################################

# import  exempale
# exempale.myline

# import sys
# print(sys.path)


# import exempale
# print(exempale.add(5,6))

# 28 -----------------------------------------------------------------------------------------------------------


# Snake water gun

# import random
# lst = ['s','w','g']

# chance = 10
# no_of_chance = 0
# computer_point = 0
# human_point = 0

# # print(" \t \t \t \t Snake,Water,Gun Game\n \n")
# print("s for snake \n w for water \n g for gun \n")

# # making the game in while
# while no_of_chance < chance:
#     _input = input('Snake,Water,Gun:')
#     _random = random.choice(lst)

#     if _input == _random: 
#         print("Tie Both 0 point to each \n ")

#     # if user enter s
#     elif _input == "s" and _random == "g":
#         computer_point = computer_point + 1
#         print(f"your guess {_input} and computer guess is {_random} \n")
#         print("computer wins 1 point \n")
#         print(f"computer_point is {computer_point} and your point is {human_point} \n ")

#     elif _input == "s" and _random == "w":
#         human_point = human_point + 1
#         print(f"your guess {_input} and computer guess is {_random} \n")
#         print("Human wins 1 point \n")
#         print(f"computer_point is {computer_point} and your point is {human_point} \n")

#     # if user enter w
#     elif _input == "w" and _random == "s":
#         computer_point = computer_point + 1
#         print(f"your guess {_input} and computer guess is {_random} \n")
#         print("computer wins 1 point \n")
#         print(f"computer_point is {computer_point} and your point is {human_point} \n ")

#     elif _input == "w" and _random == "g":
#         human_point = human_point + 1
#         print(f"your guess {_input} and computer guess is {_random} \n")
#         print("Human wins 1 point \n")
#         print(f"computer_point is {computer_point} and your point is {human_point} \n")

#     # if user enter g

#     elif _input == "g" and _random == "s":
#         human_point = human_point + 1
#         print(f"your guess {_input} and computer guess is {_random} \n")
#         print("Human wins 1 point \n")
#         print(f"computer_point is {computer_point} and your point is {human_point} \n")


#     elif _input == "g" and _random == "w":
#         computer_point = computer_point + 1
#         print(f"your guess {_input} and computer guess is {_random} \n")
#         print("computer wins 1 point \n")
#         print(f"computer_point is {computer_point} and your point is {human_point} \n ")

#     else:
#         print("you have input wrong \n")

#     no_of_chance = no_of_chance + 1
#     print(f"{chance - no_of_chance} is left out of {chance} \n")

# print("Game over")

# if computer_point==human_point:
#     print("Tie")

# elif computer_point > human_point:
#     print("Computer wins and you loose")

# else:
#     print("you win and computer loose")

# print(f"your point is {human_point} and computer point is {computer_point}")

# #
# # Snake Water Gun Game in Python
# # The snake drinks the water, the gun shoots the snake, and gun has no effect on water.
# #

# 29 ****************-----------******************---------------***************--------*************--------------******************------------------*****************************-------------------***********************-------------


# import random
# list = ['s','w','g']

# chance = 10
# no_of_chance=0
# computer_point=0
# human_point=0

# print ("s for sake\n w for water\n g for gun\n")

# # making the game in while
# while no_of_chance < chance:
#     _input = input('snake,water,gun:')
#     _random=random.choice(list)

#     if _input == _random :
#         print("Tay computer point and your point is equeal \n ")
         

#     # if user enter "s"
#     elif _input == "s" and _random == "g":
#         computer_point=computer_point + 1
#         print(f"your guess {_input} and computer guess {_random} \n")
#         print("computer wine 1 point \n")
#         print(f"computer_point is {computer_point} and your point is {human_point}\n")

#     elif _input == "s" and _random == "w":
#         human_point=human_point +1
#         print(f"your guess {_input} and compiuter guess {_random}\n")
#         print("human wine 1 point \n ")
#         print(f"computer_point is {computer_point} and your point is {human_point}\n ")

# # if user enter "w"
#     elif _input == "w" and _random == "s":
#         computer_point=computer_point +1
#         print(f"your guess {_input} and computer guess {_random}\n")
#         print("computer wine 1 point \n")
#         print(f"computer_point is {computer_point} and your point is {human_point} \n")

#     elif _input == "w" and _random == "g":
#         human_point=human_point +1
#         print(f"your guess {_input} and computer guess {_random}\n")
#         print("human wine 1 point \n")
#         print(f"computer_point is {computer_point} and your point is {human_point} \n")

# # if user enter "g"

#     elif _input == "g" and _random == "w":
#         computer_point=computer_point +1
#         print(f"you guess {_input} and computer guess {_random} \n")
#         print("computer wine 1 point \n ")
#         print(f"computer_point is {computer_point} and your point is {human_point} \n")

#     elif _input == "g" and _random == "s":
#         human_point=human_point +1
#         print(f"your guess {_input} and computer guess {_random}\n")
#         print("human wine 1 point \n")
#         print(f"coputer_point is {computer_point} and your point is {human_point} \n")

#     else:
#         print("you have input wrong \n")

#     no_of_chance = no_of_chance +1
#     print(f"{chance-no_of_chance} is left out of {chance} \n")
# print("game over")

# if computer_point==human_point:
#     print(Tie)
# elif computer_point>human_point:
#     print("computer is wine and your lose ")
# else:
#     print("you wine and computer is lose")

# print(f"your point is {human_point} and computer point is {computer_point}")


# 30 -------------------------------------------------------------class in python---------------------------------------------------------------

# class student:
#     def __init__(self,name,std,sub):
#         self.name=name
#         self.std=std
#         self.sub=sub
#     def printdeatils(self):
#         return f"name is {self.name}. standered is {self.std}. subject is {self.sub}"
#     classmethod
#     def change_leaves(cls,newleaves):
#         cls.no_of_leaves = newleaves

# Suraj = student("Suraj Nayak Raghuvanshi",1,"English,Hindi,Match,Chamistry,Physice")
# saroj = student("Saroj Nayak",10,"Hindi,English,Match,Social since,since")
# sonu= student("Sonu Nayak",12,"hindi literature,political since, geography,English")
# sonam = student("Sonam Nayak",11,"English,Hindi literature,political since,geography")

# Suraj.name = "Suraj_Nayak_Raghuvanshi"
# Suraj.std = 1 
# Suraj.collage_name = "Bhimrav Ambedkar PG collage"
# Suraj.sub = "computer","English","Physic","Chemistry","match

# saroj.name= "saroj Nayak Raghiuvanshi"
# saroj.std = 10
# saroj.sub = "Hindi","English","shocial since", "since","match"

# sonu.name = "Sid Nayak Raghuvanshi"
# sonu.std = 12 
# sonu.sub = ["hindi literature","political since", "geography","English"]

# sonam.name = "Sonam Namyak Reaghuvanshi"
# sonam.std = 10
# sonam.sub = ["Hindi", "English","Social Since","since","match",]

# print(Suraj.printdeatils())

# Suraj.change_leaves(26)

# print(Suraj.no_of_leaves)

# print(Suraj.printdeatils())
# # 31 -------------------------------------------Multiple Inheritance class-------------------------------------------------------------------

# class employee:
#     no_of_lives=8

#     def __init__(self,aname,asalari,aroll):

#         self.name = aname 
#         self.salari=asalari
#         self.roll=aroll

#     def printdeatils(self):
#         return f"name is {self.name}. salari is {self.salari}. employee roll is {self.roll}"

# class coolprogrammer(employee,student):
#     pass

# sharuk=coolprogrammer()
# suraj = employee ("Suraj",450,"Programar")
# deepash = employee ("deepash",400,"programar")
# lakhan = employee ("Lakhan",250,"worker")
# radha = employee ("Radhe",300,"manag mant")

# deepash.name ="deepash kumawat"
# deepash.salari= 555
# deepash.roll= "coading"

# lakhan.name = "Lakhan Kumawat"
# lakhan.salari = 333
# lakhan.roll = "Worker"

# radha.name = "Radhashame Kumawat"
# radha.salari = 425
# radha.roll = "menegment"

# sharuk.name= "sharuk"
# sharuk.salari=2525
# sharuk.roll="coolprogrammer"
# sharuk.std = 12
# sharuk.sub = "Hindi","English","Since","Match"
# print (suraj.printdeatils())
# print(deepash.printdeatils())

# 32 *************-------------------****** Public, Private & Protected Access Specifiers ****************------------*******************---------------------*******************

# Public -
# Protected -
# Private -

# class Employee:
#     no_of_leaves =5 
#     var = 8
#     _protec = 9
#     __pr = 98

#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole

#     def printdetails(self):
#         return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

#     @classmethod
#     def change_leaves(cls, newleaves):
#         cls.no_of_leaves = newleaves

#     @classmethod
#     def from_dash(cls, string):
#         return cls(*string.split("-"))

#     @staticmethod
#     def printgood(string):
#         print("This is good " + string)

# emp = Employee("harry", 343, "Programmer")
# print(emp.printdetails())

# 33 *************---------------**************-----------******-------------**************

# class Employee:
#     no_of_lives=8
#     _pravite=9
#     def __init__(self, name, salari, roll):
#         self.name = name 
#         self.salari=salari
#         self.roll=roll

#     def printdeatils(self):
#         return f"Name is {self.name}. salari is {self.salari} and employee roll is {self.roll}"
         
# emp = Employee("suraj", 525, "programar")
# print(emp.printdeatils())

# 34 **********************--------------******************---------------*****************--------------**************************-----------*********************--------------*******************-------------

# Super() and Overriding In Classes)

# class A:
#     Rohan1="I m a Rohan shukhla"

#     def __init__(self):
#         self.var1=" Rohan1 is a instructor of collage "
#         self.Rohan1="Instance variable in class A"
#         self.suraj=" I m Suraj"
# class B(A):
#     Rohan1="I m a Rohan Kumar"

    
#     def __init__(self):
#         super().__init__()    
#         self.var1=" Rohan2 is a instructor of collage "
#         self.Rohan1="Instance variable in class B"
#         super().__init__()
#         print(super().Rohan1)
# a=A()
# b=B()

# print(b.suraj,b.var1,b.Rohan1)

# 35 ****************-------------*********************-------------************************---------**************-----------**************************-----------***********\

# Operator Overloading & Dunder Methods

# class Employee:
#     no_of_lives=8
#     _pravite=9                                                          
#     def __init__(self, name, salari, roll):
#         self.name = name 
#         self.salari=salari
#         self.roll=roll

#     def printdeatils(self):
#         return f"Name is {self.name}. salari is {self.salari} and employee roll is {self.roll}"

#     def __add__(self,other):
#         return self.salari + other.salari 

#     def __truediv__(self,other):  
#         return self.salari / other.salari

#     def __mul__(self,other):
#         return self.salari * other.salari

#     def __mod__(self,sonu):
#         return self.salari % sonu.salari

#     def __pow__(self,sonu):
#         return self.salari ** sonu.salari

#     def __repr__(self):
#         return f"Employee ('{self.name}', {self.salari} , '{self.roll}' )"
    
#     def __str__(self):
#         return f"Name is {self.name}. salari is {self.salari} and employee roll is {self.roll}"


# emp1 = Employee("suraj", 525, "programar")
# Sonu = Employee("Sonu",325,"Programar")
# print(emp1 + Sonu)
# print(emp1 / Sonu)
# print(emp1)                                                             
# print(repr(emp1))
# print(emp1*Sonu)
# print(emp1%Sonu)
# print(emp1**Sonu)


# 36 ************------************--------***************-------------*****************-----------------**************---------------*****************---------
# r=2
# for r in range (1,8,1):
#     for j in range (1,(r+1),1):
#         print(j,"", end="")
#     print("")

# help("keywords")

#37***************************************-------------------***********************-----------------------**************************-------------------------************************-----------


# class Employee:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#         # self.email = f"{fname}.{lname}@codewithharry.com"

#     def explain(self):
#         return f"This employee is {self.fname} {self.lname}"

#     @property
#     def email(self):
#         if self.fname==None or self.lname == None:
#             return "Email is not set. Please set it using setter"
#         return f"{self.fname}.{self.lname}@codewithharry.com"

#     @email.setter
#     def email(self, string):
#         print("Setting now...")
#         names = string.split("@")[0]
#         self.fname = names.split(".")[0]
#         self.lname = names.split(".")[1]

    # @email.deleter
    # def email(self):
    #     self.fname = None
    #     self.lname = None


# hindustani_supporter = Employee("Hindustani", "Supporter")
# nikhil_raj_pandey = Employee("Nikhil", "Raj")

# print(hindustani_supporter.email)

# hindustani_supporter.fname = "US"
# print(hindustani_supporter.email)

# print(hindustani_supporter.email)
# hindustani_supporter.email = "this.that@codewithharry.com"
# print(hindustani_supporter.fname)

# del hindustani_supporter.email

# print(hindustani_supporter.email)
# hindustani_supporter.email = "Harry.Perry@codewithharry.com"
# print(hindustani_supporter.email)


# 38 *****-------------**********---------------******************------------------------******************-----------------****************--------------*******-


# class Employee:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#         # self.email = f"{fname}.{lname}@codewithharry.com"

#     def explain(self):
#         return f"This employee is {self.fname} {self.lname}"

#     @property
#     def email(self):
#         if self.fname==None or self.lname == None:
#             return "Email is not set. Please set it using setter"
#         return f"{self.fname}.{self.lname}@codewithharry.com"

#     @email.setter
#     def email(self, string):
#         print("Setting now...")
#         names = string.split("@")[0]
#         self.fname = names.split(".")[0]
#         self.lname = names.split(".")[1]
# skillf = Employee("Suraj","nayakr")
# print(skillf.email)
# print(type(skillf))
# print(id("suraj"))
# print(dir(skillf))

# import inspect # this is a inspect module
# print(inspect.getmembers(skillf))

# class student:
#     def __init__(self,name,rolnumber,Mnumber,) -> None:
#         self.StudentRolnumber=rolnumber
#         self.StudentName=name
#         self.StudentMobileNumber=Mnumber


#     def explain(self):
        
# 39*************----------------************************------------***********************-------------**********************---------------***************--------------*
# Python Comprehensions
# ls= []
# for i in range (100):
#     if i%3==0:
#         ls .append(i)
# print(ls)

# ls=[i for i in range(100) if i%3==0]
# print(ls)

# 40 ******---------*************-*-------------------------*************************************-------------------*****************************---------------******************
# dixck={i:f"Item{i}" for i in range(5)}
# dixck= {velue:key for key,velue in dixck.items() }
# print(dixck)

# socilworker={dore for dore in {"dore1","dore2","dore1","dore2","dore1","dore2"}}
# print(socilworker)

# evens=(i for i in range(50) if i%3==0) # This is a Generator object 
# print(evens)
# for item in evens:  
#     print(item)     

# 41 ******************-----------------*************************----------------------************************-------------------------*****************-------------

# using Else With For Loop

# khana = ["roti","aalu ke prante","edlidosa","sambhar"]

# for item in khana:
#     # print(item)
#     if item == "rotili":
#         break

# else:
#     print ("Itewm is not avelable in list")

# 42 **************-------------************************----------------------***************************----------------------***************************-------------

# Function Caching 

# import time
# from functools import lru_cache  
# @lru_cache(maxsize=10) # lru_caching is  decorato
# def some_work (n):
#     time.sleep(n)
#     return n
# if __name__=="__main__":
#     print("now runing some work" )
#     some_work (2)
#     some_work (2)
#     some_work (2)
#     print("Done coling agine.....")
#     some_work (3)
#     print("coling agane...")

# accepting a chiling

# import time 
# from functools import lru_cache
# @lru_cache(maxsize=5)
# def sum (n):
#     time.sleep(n)
#     return n
# if __name__=="__main__":
#     print(" add of tow nuimber ")
#     sum (2)
#     a=int(input("enter a number"))
#     sum (2)
#     b=int(input("enter second number"))
#     sum (2)
#     ab= a+b
#     print(ab)

# *************--------------------*************************--------------------***********************-------------------*********************----
# try :
#     f= open ("F:/nayak/surajn.txt")
# except EOFError as e:
#     print ("eof erro is coming",e)
# finally:
#     print("run this anway")

# 43 ***************-----------------***************************------------**************************---------------**************************-------------------*************
# # Coroutines In Python

# from typing import Text
# def sercher():
#     import time
#     book="code whit Suraj He is good boy and  he is Top class coder "
#     time.sleep(3)

#     while True:
#         text = (yield)

#         if text in book :
#             print("Your text is in the book")
#         else:
#             print("Your Text is not in the book")
# search = sercher()
# next(search)
# search.send ("He is good boy")
# input("enter aney key")
# search.send("good boy")
# input("enter aney key")
# search.send("good boy")
# input("enter aney key")
# search.send("good boy")
# input("enter aney key")
# search.send("good boy")
# ****************-------------*******************************----------------********************************--------------------------******************************---------------------****************
# import requests













# ********************-----------------*************************-----------------------********************************---------------------------***************************-------------------**************************
# json Module

# import json

# data='{"suraj":"Jaipur","hitesh":"Udaipur","Sdiarth Singh":"Utarpradesh","sidarth":"Nimbahera"}'

# parsed= json.loads(data)
# print(parsed["suraj"])

# data1={"nakul":"entelegent student","rohit":"school student","frana":"she is good girl and she is prity ",
#       "monu":["he is very fety boy ","he is eating fodd ","as like chaken,piza,buger"],"bharat_gayri":"he is very hard worker boy "}
# js=json.dumps(data1)
# print(js)

# *************------------*************************--------------******************************-----------------***********************--------------------****************************------------------------*******************

# import pickle

# carlist = ["BMW","Marsdis","odi","TATA","KEA","frari"]
# file="Mycar.pkl"
# fileobj=open(file,'wb')
# pickle.dump(carlist,fileobj)
# fileobj.close()

# file="Mycar.pkl"
# fileobj=open(file,'rb')
# mycar= pickle.load(fileobj)
# print(mycar)

# *****************-------------------**************************----------------***************************-----------------****************************************-----------------****************************---------------------****************-
# def speak(str):
#     from win32com.client import Dispatch
#     speak=Dispatch("SAPI.SpVoice")
#     speak.Speak(str)
# if __name__=="__main__":
#     speak("Kailash chandra nayak you are hardworker and you are grate father")

# ***********------------********************----------------------**************************---------------**********************------------------*/*****************---------

#  By useing Raise exception handile !

# a=input("what is you are name ?")
# b=input("how much do ypu earn ?")
# if int(b)==0:
#     raise ZeroDivisionError("Numbers are not allowed")
# print(f"Hello{a}")

# ----------------------------------------------
# c=input("Enter You Are Name")

# try:
#     print (a)
# except Exception as e:

#     if c == "number" :
#         raise ValueError("number is not wright ")
#     print("Exception Hendel")

# ***************---------------*****************-----------------************************-----------------------*********************---------------

# Email colectur
# Regex Extractor Email

# import re

# str = '''Skip to main contentAccessibility help
# Accessibility feedback
# Google
# IT company in udaipur

# All
# MapsNewsImagesShoppingMore
# Tools
# About 4,06,00,000 results (0.65 seconds) 
# Map of IT company in udaipur
# WebSenor - Website development company, Web desIgn company in Udaipur
# 4.9 
#  (383) · Software company
# Lodha S.M. Complex, 3rd, Post Office Road · 099508 34560
# Open ⋅ Closes 7PM

# "One of the best IT company"
# Website
# Directions
# Elixir Technologies Pvt. Ltd.- Web Design & Development Company, SEO Digital Marketing Agency Udaipur
# 4.9 
#  (524) · Software company
# Vijay Enclave, Plot No. 721 Gavri Circle · 092514 32003
# Open ⋅ Closes 7:30PM

# "Best IT company in udaipur Rajasthan ."
# Website
# Directions
# ARE InfoTech - IT companies in Udaipur, Digital Marketing Company, SEO Company, Website Design
# 4.9 
#  (8) · Software company
# 2nd floor, 6, Chetak Cir, Near Moon Light Dry Cleaners · 091065 81915
# Temporarily closed

# "One of the best company for digital marketing solution especially for SEO."
# Directions
# View all

# Top 15 IT Companies in Udaipur - My Udaipur Cityhttps://myudaipurcity.com › Career
# Top 15 IT Companies in Udaipur · Advaiya · Elixir · 3i planet · Arcgate · Obbserv · Cognus · E Connect · Websenor Infotech ...
# ‎Top 15 IT Companies in Udaipur · ‎Advaiya · ‎Aspire Techno Solutions · ‎Baymediasoft

# Top 15 IT Companies in Udaipurhttps://www.udaipurtalky.com › Career
# Top 15 IT Companies in Udaipur · 1.1 Obbserv · 1.2 Advaiya · 1.3 E Connect · 1.4 Cognus · 1.5 Baymediasoft · 1.6 Technetizens · 1.7 Elixir · 1.8 IFW ...
# 30-Jun-2018 · Uploaded by Obbserv
# ‎List of IT companies in Udaipur · ‎Obbserv · ‎Baymediasoft · ‎IFW webstudio

# Top 5 IT Companies In Udaipur, Rajasthan, India - Elixir ...https://www.elixirinfo.com › blog › top-it-companies-in...
# Top 5 IT Companies In Udaipur, Rajasthan, India · Elixir Technologies Pvt. Ltd. · WebSenor · 3i Planet · Advaiya · Baymediasoft ...

# Top Information Technology Companies in Udaipur, Rajasthanhttps://www.glassdoor.co.in › Explore › top-informatio...
# Top Information Technology Companies in Udaipur, Rajasthan · Genpact · Metacube Software Pvt. Ltd. · ATCS · Google · Microsoft · Salesforce · Flipkart · Dell ...

# Software Companies in Udaipur City - Justdialhttps://www.justdial.com › ... › 134+ Listings
# 134 Software Companies in Udaipur City, Udaipur-Rajasthan. Find ✓Internet Website Designers, ✓Internet Website Developers, ✓Computer Software Developers, ...
#  Rating: 4.8 · ‎1,375 votes

# IT Companies jobs in Udaipur, Rajasthan - Indeedhttps://in.indeed.com › IT-Companies-jobs-in-Udaipur,-...
# 84 IT Companies jobs available in Udaipur, Rajasthan on Indeed.com.

# List of IT Services/ IT Companies in Udaipur - Yellow Pageshttps://yellowpages.webindia123.com › Udaipur
# Udaipur IT Companies. Find address, phone number, timing, email . Photos, videos and deals of Udaipur IT Companies, Rajasthan, India like World SEO Services ...

# Best Software Development Company in India - Udaipurhttps://www.websenor.com › best-software-companies-...
# Websenor InfoTech is a Udaipur, India based software development and outsourcing company that focuses on highly qualitative, timely delivered, and cost- ...

# Apply to 208 It Park Jobs In Udaipur on Naukri.comhttps://www.naukri.com › ... › it park Jobs In udaipur
# Explore It Park Job Openings In Udaipur Now! ... Kota, Udaipur, Jaipur ... responsibility; business development executive; client; company. 30+ Days Ago.

# Top 11 Most Promising IT Companies in Udaipur [2021]https://www.tarangsoft.com › it-companies-udaipur
# 17-Mar-2021 — 1 PapaSiddhi · 2 Object Developer · 3 Appsenor · 4 Splix Cube · 5 Yug Technology · 6 Webyot Technologies · 7 Wizorbot · 8 TarangSoft Solutions LLP ...
# Related searches
# top mnc companies in udaipur
# software company in udaipur 
# best software company in udaipur
# top it companies in udaipur
# digital marketing company in udaipur
# it companies in udaipur for internship
# it companies in jodhpur
# elixir udaipur
# 1	
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# Next
# India
# Raza Colony, Nimbahera, Rajasthan - Based on your places (Work) - Update location
# HelpSend feedbackPrivacyTerms


# Skip to main contentAccessibility help
# Accessibility feedback
# Google
# indian oil

# All
# NewsMapsImagesShoppingMore
# Tools
# About 1,54,00,00,000 results (0.72 seconds) 

# Indian Oil Corporation Ltd. : IndianOil : Iocl.comhttps://iocl.com
# Welcome to the world of IndianOil, an integrated oil company in India and across the globe has its presence in almost all the streams of oil, gas, ...
# Results from iocl.com
# Latest Job Openings
# HR/MED/37/2021-22 List of eligible candidates for Walk in ...
# RO KSK Dealerships
# Requirement of land for Retail Outlet (Petrol /Diesel Pump) in ...
# LPG Services
# LPG Services. Support. Indane LPG · Indane Transparency ...
# Apprenticeships
# Notification for Engagement of Technical and Non-Technical ...
# Careers @IndianOil
# IndianOil offers a world of opportunities across more than ...
# Contact Us
# IndianOil is an Indian public sector oil and gas company ...
# Map of indian oil
# A
# Nakoda Filling Station (Indian Oil)
# Chittaurgarh Road, Near, JK Cement, Kailashnagar · 094614 20236
# Open 24 hours
# Website
# Directions
# B
# Balaji Indian Oil -IOCL Petrol Pump
# Rajasthan · 094405 66707
# Open 24 hours
# Directions
# C
# Heena Indian Oil
# Rajasthan · 097995 24786
# Directions
# View all
# People also ask
# Is Indian Oil same as indane?

# Who is the CEO of Indian Oil?



# Feedback

# Indian Oil Corporation - Wikipediahttps://en.wikipedia.org › wiki › Indian_Oil_Corporation
# Indian Oil Corporation Limited (IOCL), d/b/a IndianOil, is an Indian government corporation. It is under the ownership of Ministry of Petroleum and Natural ...

# Indian Oil Corp Ltd (@IndianOilcl) · Twitter
# https://twitter.com/IndianOilcl
# Media posted by Indian Oil Corp Ltd
# Proper nutrition is essential for a happy and healthy life. This #NationalNutritionWeek, let's pledge to adopt a healthy lifestyle and spread awareness on the value of good nutrition & #health.
# Twitter · 15 mins ago
# Media posted by Indian Oil Corp Ltd
# Media posted by Indian Oil Corp Ltd
# Media posted by Indian Oil Corp Ltd
# Media posted by Indian Oil Corp Ltd
# #IndianOil's Marketing Head Office is illuminated on the eve of #62ndIndianOilDay celebrations. Fuelling India's growth with trust. Celebrating India and #IndianOil! #PehleIndianPhirOil
# Twitter · 10 hours ago
# Media posted by Indian Oil Corp Ltd
# Media posted by Indian Oil Corp Ltd
# Media posted by Indian Oil Corp Ltd
# Media posted by Indian Oil Corp Ltd
# #IndianOil's Corporate Office, New Delhi shines brightly as part of the #62ndIndianOilDay celebrations. 62 years of serving the Nation, keeping its promise of energising India today & tomorrow. #PehleIndianPhirOil
# Twitter · 12 hours ago
# Media posted by Indian Oil Corp Ltd
# Mariyappan Thangavelu brought more glory for #TeamIndia as he won a silver medal at the #Tokyo2020  #Paralympics  in men's high jump event. #IndianOil congratulates him on winning this historic Laurel for the country. #Praise4Para  #PehleIndianPhirOil
# Twitter · 13 hours ago
# Media posted by Indian Oil Corp Ltd
# Sharad Kumar clinched the bronze medal with an effort of 1.83 metres in men’s high jump at #Tokyo2020 #Paralympics. #IndianOil congratulates him for his outstanding performance. #Praise4Para  #PehleIndianPhirOil
# Twitter · 13 hours ago
# View on Twitter

# Indian Oil Corporation Ltd. - The Economic Timeshttps://economictimes.indiatimes.com › stocks › compa...
# Indian Oil Corp. share price live updates on The Economic Times. ... Get detailed Indian Oil Corp. stock price news and analysis, Dividend, Bonus Issue, ...

# Latest News, Videos and indian oil Photos | Times of Indiahttps://timesofindia.indiatimes.com › topic › indian-oil
# The Indian Oil Business includes - refining, pipeline transportation, marketing of petroleum products, exploration and production of crude oil, natural gas and ...
# Top stories

# Hindustan Times Auto News
# .
# To meet India's fuel demand, Indian Oil Corp plans ₹1 lakh crore investment
# .
# 1 day ago


# The Economic Times
# .
# Indian Oil Corp. shares up 1.42% as Nifty gains
# .
# 1 day ago


# Zee News
# .
# IOCL Recruitment 2021: Last date today to apply for 480 Apprentice posts in Indian Oil, details at iocl.com
# .
# 3 days ago


# Times of India
# .
# Indian Oil expands JV with Malaysia's Petronas to focus on LNG plants
# .
# 4 days ago


# The Financial Express
# .
# Indian Oil Corporation rating – Hold: Q1 consolidated EPS up 2.7x y-o-y
# .
# 3 weeks ago


# Zee Business
# .
# Indian Oil Corporation to build Indias first green hydrogen plant - All you need to know
# .
# 1 week ago


# The Financial Express
# .
# Why govt is not cutting petrol, diesel prices; Rs 1.3 lakh cr oil bond repayments due for cheap fuel in past
# .
# 1 month ago


# The Financial Express
# .
# Zomato, Tata Steel, BPCL, Indian Oil, Yes Bank, Tata Power, Chemplast, Aptus IPOs, IRCTC stocks in focus
# .
# 3 weeks ago


# BloombergQuint
# .
# Indian Oil Q1 Results: Profit Falls 32% On Lower Demand, Other Income
# .
# 1 month ago

# View all

# Indane LPG - Indian Oil websitehttps://cx.indianoil.in › webcenter › portal › Customer
# Related searches
# indian oil login
# iocl
# indian oil career
# indian oil share price
# indian oil offer
# indian oil partner
# indian oil gas
# indian oil dealer login
# 1	
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# Next
# Indian Oil Corporation
# Petroleum refining company
# Skip to main contentAccessibility help
# Accessibility feedback
# Google
# email id of indian oil

# All
# NewsMapsImagesVideosMore
# Tools
# About 9,54,00,000 results (0.70 seconds) 
# Indian Oil Corporation Ltd. Company Profile, Address and Other Details
# Address Descriptor	Registered Office
# Telephone	26447616
# Fax	26447961
# Email	Investors@indianoil.in
# Website	Http://www.iocl.com
# 45 more rows

# Indian Oil Corporation Ltd. Company Profile, Address and ...https://www.goodreturns.in › ... › Quotes
# About featured snippets
# •
# Feedback

# Contact Us : IndianOil | Oil and Gas Company in India - Iocl.comhttps://iocl.com › contact-us
# IndianOil is an Indian public sector oil and gas company headquartered in New Delhi. Our business interests overlap the entire hydrocarbon value-chain, ...
# ‎Vigilance Queries · ‎FAQs

# Business Enquiries - Iocl.comhttps://iocl.com › pages › BusinessEnquiry
# Indian Oil Corporation Ltd. IndianOil Bhavan, 1, Sri Aurobindo Marg, Yusuf Sarai, New Delhi 110016. Tel: 91-11-26531082. Email: ...

# Help : IndianOil - Iocl.comhttps://iocl.com › help
# Copyright © Indian Oil Corporation Ltd Site Map | Terms of Use | Data Privacy Policy | Hyperlinking Policy. Last updated on 31/08/2021 11:24 AM Toll FREE ...
# People also ask
# How do I contact Indian Oil?
# How can I complain to Indian Oil?

# How do I contact Indian Oil petrol pump dealer?

# How can I complain to indane gas?

# Feedback

# petroleum.nic.in/sites/default/files/cpio_details.pdfhttp://petroleum.nic.in › sites › default › files › cpio_details

# Indian Oil Contact Details, Toll Free Number, Email ID, and Morehttps://contactdetailswala.in › indian-oil-contact-details
# 18-Aug-2018 — Office Address Of Indian Oil · Corporate Office Address: Indian Oil Corporation Limited, 3079/3, Sadiq Nagar, J.B. Tito Marg, New Delhi-110049 ...

# IOCL Toll Free Number, State Wise Office Address / Branches ...https://customercarenumber.freshersnow.com › iocl
# Indian Oil Corporation Limited | West Bengal Office Address — IndianOil Bhavan, 139, Mahatma Gandhi Road, Chennai – 600 034. Indian Oil Corporation ...

# Indane Gas Complaint Number - BankBazaarhttps://www.bankbazaar.com › Gas Connection
# The Indian Oil Corporation has proved time and again that it is one of the best ... Enter your name, address, email id, mobile number, name of the state, ...

# Public Sector Undertaking, Indian Oil Corporation Limitedhttps://www.sarkaritel.com › psu › psudetail › psu_id=1...
# Registered Office: G-9, Ali Yavar Jung Marg, Bandra (East), Mumbai - 400051. Website: http://www.iocl.com E-mail: iocl.cocc@indianoil.in ...
# Images for email id of indian oil

# indane gas

# gas agency

# gurmeet singh

# lpg gasgas cylinder

# corporation limited

# ioc

# petrol pumpindane lpg

# corporation ltd

# portal

# login

# kamal kumar

# refinery

# iocl
# Image result for email id of indian oil
# Image result for email id of indian oil
# Image result for email id of indian oil
# Image result for email id of indian oil
# Image result for email id of indian oil
# Image result for email id of indian oil
# Image result for email id of indian oil
# Image result for email id of indian oil
# Image result for email id of indian oil
# Image result for email id of indian oil
# View all
# Feedback
# View all
# Related searches

# Indian Oil Corporation Ltd. Bonga...

# Chennai Petroleum Corporatio...

# Lanka IOC

# Indian Oil Petronas Private Li...

# Indian Synthetic Rubber Li...

# IndianOil LNG Private Limited
# See more
# Feedback
# indane gas complaint mail id
# indian oil customer care email id
# indian oil corporation limited contact details pdf
# indian oil head office contact number
# indian oil login
# indian oil corporation head office address
# indian oil head office mumbai
# iocl chairman contact details
# 1	
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# Next
# India
# Raza Colony, Nimbahera, Rajasthan - Based on your places (Work) - Update location
# HelpSend feedbackPrivacyTerms
# '''

# email= re.findall(r"[0-9a-zA-Z._+:+//]+[.][a-zA-Z]+",str)
# print(email)
#
# ******************-------------------************************--------------**********************-----------**********************************----------------***********************----------------

