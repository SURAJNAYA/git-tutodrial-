# name=input("type your name")
# print ("hello" + name)
# age= input("what is your age ?")
# # print("your age is",age) 
# number_first = int(input("enter first number"))
# number_sec = int(input("enter second number"))
# total= number_first + number_sec
# print("totle is" + str(total))
# print(f"totle number {total}  ")
# num1=int(input("enter first number "))
# num2=int(input("enter second number"))
# num3=int(input("enter there number"))

# average=nun1+num2+ num3 //3
# print("average is",average )
# num1,num2,num3= input("enter three number").split(",") # seprited by coma ','
# print(f"average is : { (int(num1) + int(num2) + int(num3)) /3}")

#  dictionary is nothing key velue pairs

# d1 = {"suraj":{"L":"senvich","B":"megge","D":"fesh"},"mohit":{"L":"pizaa","B":"gobi","D":"Bhindi"},
#  "mother":{"L":"eig","B":"fesh","D":"chaken"},"papa":"leadyfinger"}
# d1["lk"]="junkfood"
# print(d1)
# # del d1 ["lk"]
# # print(d1)  
# # d1.update({"radhe":"coffe"})
# # print (d1)
# # print (d1.keys())
# # print (d1.items())
# print ( " what is your age ")
# age = int (input ())
# if age < 18:
#     print("you can't drive ")

# elif age== 18:
#     print("we will thing about it ")

# else:
#     print ("You Can Drrive ")
 
# a=int(input("enter your age"))
# if a>18 and a<100:
#     print("YOU CAN DRIVE :)")
# elif a==18:
#     print("WE CANNOT DECIDE WETHER YOU ARE ELIGIBLE FOR DRIVING OR NOT")
# elif a<18:
#     print("Legeally,YOU ARE NOT AUTHORIZED TO BE A DRIVER")
# else:
#     print("Illogical age")




# faulty calculater

# 45*3=55,56+9=77 ,56/6=4




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

# list3 = [ ["suraj","piza"],["sonu","buger"],["sonam","magge"]]
# for item,lunch in list3 :
    # print(item,";Lunch Food Name is",lunch)

#   loop statment 

# a=int(input("enter a number "))
# while a<100:
#     print(a)
#     a=a+1
# print("condition folse")

# The Breck Statment

# a=int(input("enter a number "))
# while a<100:
    # if (a==50):
        # break
    # print(a)
    # a=a+1
# print("condition folse")



# while(True):
#     ab=int(input("enter a number \n"))
#     if ab>100:
#         print("congrtulation you are enter grater then 100\n")
#         break
#     else:
#             print("try agane\n")
#             continue



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


# Operators In Pythons
# Arithmetic Operators
# Assignment Operators
# Comparison Operators
# Logical Operators
# Identity Operators
# Membership Operators
# Bitwise Operators

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
# x %=7 # x = x%7
# psrint(x)

# Comparison Operators
# from typing_extensions import Concatenate


# i = 5


# Logical Operators
# a = True
# b = False

# Identity Operators
# print(5 is not 5)

# Membership Operators
# list = [3, 3,2, 2,39, 33, 35,32]
# print(324 not in list)

# Bitwise Operators
# 0 - 00
# 1 - 01
# 2 - 10
# 3 - 11

# 1print(0 & 2)
# print(0 | 3)



# a=int(input("enter number a\n"))
# b=int(input("enter number b \n"))
# print("B A se bada he bhai") if a<b else print("A B se bada hei bhai")


# def function1 (a,b):
#     """The Function whicle will calculate sum  of two number(this is a docstringty,hjmh`) """
#     print(" Sum Number is ",a+b)
# function1(1,9)
# print(function1.__doc__)




# def function2 (a,b):
#     """The Function whicle will calculate average of two number""" 
#     avrage= (a+b)/2
#     print(avrage)
#     return avrage
# v=function2(12,6 )
# print(v)
# print(function2.__doc__)




# try except handling

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
    # print(line)
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
# contant=(f.readlines())# All Line print in row line  
# print(contant)
# f.close()


# f = open("surajn.txt","a")
# a=f.write("suraj is good boy and locking is outstanding \n")
# print(a)
# f.close()


# Handle read and write both 

# f = open("suraj.txt","r+")
# print(f.read())
# f.write("thenk you ")
# f.close()

# print star pattern 

# print("pattern printing")
# n=int(input("enter a  number in star partan "))
# boolean=input("true (1) or false(0)")
# if boolean=="1":
#     for i in range(1,n+1):
#         print("*" " "*i)
# if boolean=="0":    
#     for i in range(n,0,-1):
#         print("*" " "*i)

      
# globle variable

# l=15 # global variable
# def function1(n):
#     # l=5    #Local
#     m=10   #Local
#     global l
#     l=l+50
#     print(l,m)
#     print(n,"suraj")
# function1("my name is")



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



  



# recurction function in factorial 
# def recurctive_factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n * recurctive_factorial(n-1)
# number=int(input("Einrt The Number"))
# print("Factorial use iterative Mathod", number)

# Helth Managemant system

# import datetime
# def gettime():
    # return datetime.datetime.now()
# def take(k):
#     if k==1:
#         c=int(input("enter 1 for excersise and 2 for food"))
#         if(c==1):
#             value=input("type here\n")
            # with open("harry-ex.txt","a") as op:
#                 op.write(str([str(gettime())])+": "+value+"\n")
#             print("successfully written")
#         elif(c==2):
#             value = input("type here\n")
            # with open("harry-food.txt", "a") as op:
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
            # print("successfully written")
    # else:
#         print("plz enter valid input (1(harry),2(rohan),3(hammad)")
# def retrieve(k):
#     if k==1:
#         c=int(input("enter 1 for excersise and 2 for food"))
#         if(c==1):
#             with open("harry-ex.txt") as op:
#                 for i in op:
#                     print(i,end="")
#         elif(c==2):
#             with open("harry-food.txt") as op:
#                 for i in op:
#                     print(i, end="")
#     elif(k==2):
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if (c == 1):
#             with open("rohan-ex.txt") as op:
#                 for i in op:
#                     print(i, end="")
#         elif (c == 2):
#             with open("rohan-food.txt") as op:
#                 for i in op:
#                     print(i, end="")
#     elif(k==3):
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if (c == 1):
         
#             with open("hammad-ex.txt") as op:
#                 for i in op:
#                     print(i, end="")
#         elif (c == 2):
#             with open("hammad-food.txt") as op:
#                 for i in op:
#                     print(i, end="")
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



################################Built In Modules##################################################################

# import random
# random_number= random.randint(0,10)
# print(random_number)

# list = ["SUB","sub","UTV","UTV Action","Star Gold"]
# choicee=random.choice(list)
# print(choicee)


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

#  Program to print Fibonacci 
# series in reverse order 

# def fibreverse(n):
#     a=[0]*n
#     a[0]=0
#     a[1]=1

#     for i in range(2,n):
#         a[i] = a[i-2]+a[i-1]
#     for i in  range(n-1, -1, -1):
#         print(a[i] ,end= " , ")
# n=int(input("Ednter A Fibonacci Number"))
# fibreverse(n)


######################## *args / **kwargs in python###########################################################

# def funargs(*surj):
#     for item in suraj:      
#         print(item)
#  Grocery=["Dio","Solt","Asafoetida"]
#  funargs(*Grocery)
   
# def fun(*suraj):
#     print(n)
#     for item in suraj:
#         print(item)
# n="This is a Monthily Grocery Items "
# grocery_Items=["Rice","Cheni","Daal","Fennel","Cumin","red Chilli"]
# fun(*grocery_Items)


########################################### use of import ##############################################

# # import  exempale
# exempale.myline

# import sys
# print(sys.path)


# import exempale
# print(exempale.add(5,6))

# ************************************** map function ******************************************************

# num = [2,6,5,48,55,25,3,62]
# square = list(map(lambda x: x*x, num))
# print (square)


# def square(a):
#     return a*a
# def cube(a):
#     return a*a*a

# fun=[square,cube]
# num=1,2,3,4,5,6,7,89,9
# for i in  range (5):
#     val= list(map(lambda x:x(i),fun))
#     print(val)

#************************************ Filter *****************************************************************

# list_1=[1,2,3,4,5,6,7,8,9,10]

# def is_greater_5(num):
#     return num>5
# gr_then_5 = list (filter(is_greater_5,list_1))
# print(gr_then_5)

#------------------------------------REDUCE----------------------------------------------------------------------
# from functools import reduce
# list1 = 1,2,3,4,5,6,7,8,9
# num=reduce(lambda x,y:x+y,list1)
# print(num)


#--------------------------------------------------------------------------------------------------------

# Snake water gun

import random
lst = ['s','w','g']

chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0

print(" \t \t \t \t Snake,Water,Gun Game\n \n")
print("s for snake \nw for water \ng for gun \n")

# making the game in while
while no_of_chance < chance:
    _input = input('Snake,Water,Gun:')
    _random = random.choice(lst)

    if _input == _random:
        print("Tie Both 0 point to each \n ")

    # if user enter s
    elif _input == "s" and _random == "g":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    elif _input == "s" and _random == "w":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    # if user enter w
    elif _input == "w" and _random == "s":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    elif _input == "w" and _random == "g":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    # if user enter g

    elif _input == "g" and _random == "s":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")


    elif _input == "g" and _random == "w":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    else:
        print("you have input wrong \n")

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance} \n")

print("Game over")

if computer_point==human_point:
    print("Tie")

elif computer_point > human_point:
    print("Computer wins and you loose")

else:
    print("you win and computer loose")

print(f"your point is {human_point} and computer point is {computer_point}")

#
# Snake Water Gun Game in Python
# The snake drinks the water, the gun shoots the snake, and gun has no effect on water.
#

  