# ----------------------------- 28. File Handling -----------------------------

# file = open("G:/Course/Week#03/xtfile.txt", "r")
# print(file.read())           # reading file

# file = open("G:/Course/Week#03/xtfile.txt","r")
# print(file.readline())         # read only one line from start
# print(file.readline())         # read the next line and so on

# file = open("G:/Course/Week#03/xtfile.txt", "r")
# for i in file:
#     print(i)                   # will read line by line

# ----------------------------- 29. Classes and Objects -----------------------------
# class me sab objects aaty hein like:
#   Animal is a class then cat, horse, dog, parrots or zebra are objects
#   There are attributes mean further and methods to how they work.
#   Setter and getter - constructor

# class Employee:            #we should write it in capitalize form!
#     def __init__(self, name, age):          # SETTER function - self is a reference operator - __init__ this is a constructor
#         self.name = name                  #we put self cuz we make it to call it in anyother function as well.
#         self.age = age
# # allows you to access attributes and methods on the same object

#     def getEmp(self):                     # GETTER function
#         print(f"{self.name} : {self.age}")

# ab = Employee("Irbaz", 22)
# ab.getEmp()

# class Car:
#     def __init__(self, name, model):
#         self.name = name
#         self.model = model
#     def getCar(self):
#         print(f"Your car name is: {self.name} and model is: {self.model}")

# class Bus:
#     def __init__(self, name, model):
#         self.name = name
#         self.model = model
#     def getBus(self):
#         print(f"Your bus name is: {self.name} and model is: {self.model}")
    
# c = Car("Kia", "Sportage")
# b = Bus("Daewoo", "Bus LX-1334")
# c.getCar()
# b.getBus()

# ----------------------------- 30. Inheritance -----------------------------
# class Animal:
#     def __init__(self, name):
#         self.name = name

# class Cat(Animal):
#     def __init__(self, name):
#         self.name = name
#     def sound(self):
#         print(f"Animal is {self.name} and it sounds like Meowwwww 🐈")

# class Dog(Animal):
#     def __init__(self, name):
#         self.name = name
#     def sound(self):
#         print(f"Animal is {self.name} and it sounds lik Bhaoo! Bhaoo! 🐕")

# ab = Cat("cat")
# ac = Dog("dog")

# ab.sound()
# ac.sound()

# Polymorphism ka matlab he keh jo method Parent me he or wahi function child class me bhi he or wo overwrite ho jae to isy polymorphism kehty hein!


# Practicals
# CODE # 01
# class Sum:
#     def getNum(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
#     def setNum(self):
#         print(f"Your sum output is {self.num1 + self.num2}")

# n1 = int(input("Enter number 1: "))
# n2 = int(input("Enter number 2: "))
# add = Sum()
# add.getNum(n1, n2)
# add.setNum()

# CODE # 02
# Create a class Book that stores book title, author, and pages. Add a method to display all information.
# class Book:
#     def book_info(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#     def show(self):
#         print(f"""----------------- BOOK DETAILS -----------------
#             Book Title: {self.title}
#             Book Author: {self.author}
#             Book Pages count: {self.pages}
# ----------------------------------------------------""")

# b_t = input("Enter the book title: ")
# b_a = input("Enter the author of that book: ")
# b_p = input("How many pages it has: ")
# bookk = Book()
# bookk.book_info(b_t, b_a, b_p)
# bookk.show()

# CODE # 03

# class Employee:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def setEmp(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")

# values = int(input("How many user you want enter: "))
# for i in range(1, values + 1):
#     n = input(f"Enter employee name {i}: ")
#     agae = input(f"Enter age of the employee {n}: ")
#     aa = Employee(n, agae)
#     aa.setEmp()

# CODE # 04

class arb:
    def __init__(self, *values):
        self.values = values

#name, age and marks... use **kwargs... display