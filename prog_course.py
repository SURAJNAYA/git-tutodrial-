# with out argumant function

# def deatilas ():
#     print("My Name is Suraj Nayak Raghuvanshi " )
# deatilas()

# with argument function 

# def deatils(name,roll,standerde):
#     print("student name is ",name)
#     print("student roll number is",roll)
#     print("student class is ",standerde)
# deatils("suraj",121,12)

# def sum(a,B):
#     print("sum is ",a+B)
# sum(25,4005)

# def calculation (a,b):
#     print("addition is ",a+b)
#     print("subtraction is ",a-b)
# calculation(25,25)


# from random import choice


# def rec_function(n):
#     if n<=1:
#         return n
#     else:
#         n+rec_function(n-1)
# rec_function(1)


# Python program to find the sum of natural using recursive function

# def recur_sum(n):
#    if n <= 1:
#        return n
#    else:
#        return n + recur_sum(n-1)

# # change this value for a different result
# num = 10

# if num < 0:
#    print("Enter a positive number")
# else:
#    print("The sum is",recur_sum(num))

# lambda function

# n=lambda a,b:a+b
# print(n(5,6))


# module 

# import random
# n=random.randint(100,5000)
# print(n)

# import random
# movi_chanal_list=["soni sub","stargold","star plase","utv action","utv action"]
# n=random.choices(movi_chanal_list)
# print(n)


# from random import shuffle
# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# shuffle(color)
# print(color)


# import random
# number_list = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
# print ("Original list : ",  number_list)

# random.shuffle(number_list) #shuffle method
# print ("List after shuffle  : ",  number_list)

# opps in python assignment

# 1 example

# class vehicle ():
#     VEHICLE_NAME= " "
#     VEHICLE_NUMBER = 27 
#     VEHICLE_COLLAR= ""
#     def getdeta(self):
#         self.VEHICLE_NAME=input("enter vehicle name:")
#         self.VEHICLE_NUMBER=input("enter  vehicle number:")
#         self.VEHICLE_COLLAR=input("enter collar:")   
#     def display_vehicle(self):
#         print("vehicle name",self.VEHICLE_NAME)
#         print("vehicle number",self.VEHICLE_NUMBER)
#         print("vehicle collar",self.VEHICLE_COLLAR)

# vg=vehicle()
# vg.getdeta()
# vg.display_vehicle()

# 2 example

#     class vehicle():
#     pass
#     print("noven argumant")
# ob=vehicle()

# class simple program

# class vehicle():
#     def max_speed(self):
#         print("vehicle speedc is 200 km/her")
#     def mileage(self,a,b):
#         print("sume is",a+b)
# ob=vehicle()
# ob.max_speed()
# ob.mileage(45,26)

# class student():
#     def student_data(self,id,rollno,name):
#         self.id=id
#         self.rollno=rollno
#         self.name=name
#     def culact_data(self):
#         print("student id ",self.id)
#         print("student roll number is :",self.rollno)
#         print("student name is ",self.name)
# ob=student()
# ob.student_data(20,15,"mohit")
# ob.culact_data()

# thise is a 4 example of oops

# class vehicle():
#     def max_speed(self,vehicleno,vehiclename):
#         self.ve_no=vehicleno
#         self.ve_name=vehiclename
#     def mileage(self):
#         print("vehicle number",self.ve_no)
#         print("vehicle name",self.ve_name)

# class bus(vehicle):
#     def max_passenger(self,total_passenger,tikit_price):
#         self.passanger=total_passenger
#         self.tikit=tikit_price
#     def collect_data(self):
#         print("bus total passenger",self.passanger)
#         print("bus ticket price is ",self.tikit)
# ob=bus()
# ob.max_speed(1212,"mhendra")
# ob.mileage()
# ob.max_passenger(25,120)
# ob.collect_data()

# singe inheritance

# class A():
#     def Adeta(self):
#         print("deta is A")
# class B(A):
#     def Bdeta(self):
#         print("detan is B")
# ob=B()
# ob.Adeta()
# ob.Bdeta()

# Multi level inhetritance

# class A():
#     def Adeta(self):
#         print("deta is A")
# class B(A):
#     def Bdeta(self):
#         print("detan is B")
# class c(B):
#     def Cdeta(self):
#         print("deta is C")
# ob=c()
# ob.Adeta()
# ob.Bdeta()
# ob.Cdeta()

# hrachical 

# class A():
#     def Adeta(self):
#         print("deta is A")
# class B(A):
#     def Bdeta(self):
#         print("detan is B")
# class c(A):
#     def Cdeta(self):
#         print("deta is C")
# ob=c()
# ob.Adeta()
# ob.Cdeta()

# multyple inhetritance

# class A():
#     def Adeta(self):
#         print("deta is A")
  
# class B():
#     def Bdeta(self):
#         print("detan is B")
# class c(A,B):
#     def Cdeta(self):
#         print("deta is C")
# ob=c()
# ob.Bdeta()
# ob.Adeta()
# ob.Cdeta()

# multyple inhetritance specile case

# class A():
#     def Adeta(self):
#         print("deta is A")
#     def gatedeta(self):
#         print("collact deta A")
# class B():
#     def Bdeta(self):
#         print("detan is B")
#     def gatedeta(self):
#         print("collact deta B")
# class c(B,A):
#     def Cdeta(self):
#         print("deta is C")
# ob=c()
# ob.gatedeta()


from os import read, remove


# file=open("test.txt","r")
# print("file is created")
# print(file.read())

remove("test.txt")