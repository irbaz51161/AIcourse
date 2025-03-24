# ------------------- 01 - Dsiplay the result to output -------------------
# print('Hello World!')
# print(424)
# print(True)
# print(type(312.32))

# ------------------- 02 - Legal name of variables -----------------------
# name = "Irbaz"
# firstName = "zubair"    #camel case;
# FirstName = "margret"   #pascal case;
# first_name = "rameez"   #snake case;
# name1st = "areeba"      #number case; case sensitive;

# ------------------- 03 - Illegal name of variables ----------------------
# _name = "imtnan"
# 2ndName = "razi"
# $name = "opera"
# name@name = "borgois"

# ------------------- 04 - Type of variables ------------------------------
# print(type("this type"))
# print(type(34))
# print(type(65.43))
# print(type(False))

# ------------------- 05 - Data types in Python ---------------------------
# a = "string"                               #string
# b = 43                                     #integer
# c = 32.55                                  #float
# d = False                                  #boolean
# e = 1j                                     #complex
# f = ["irbaz", "raheel", "faiz"]            #list = array | index = total length - 1 | index = 2 & length = 3 | mutable
# g = ("hello", "world", "!")                #tuple | immutable
# h = {"name":"ashlie sun", "age":21}        #dictionary | "key":"value" | mutable 
# i = b"hello world"                         #bytes
# j = {"hi", "many", "flights"}              #set | it will print random list
# print(f"Length: {len(f)}")                 #length
# print(f"Index: {len(f) - 1}")              #index
# [] = square braces | () = parenthesis or round braces | {} = curly braces

# ------------------- 06 - Math operation ---------------------------------
# a = 3
# b = 3
# print(a ** b)

# ------------------- 07 - Input types ------------------------------------
# a = input("Enter input: ")
# print(a)

# ------------------- 08 - if Condition -----------------------------------
#                        CODE # 01
# num = int(input("Enter number: "))
# if (num >= 45 and num <= 50):
#     print("You are passed!")
# elif (num >= 90 and num > 101):
#     print("Your are passed with Grade: A! Congratulations!")
# else:
#     print("You are failed!")

#                        CODE # 02
# num = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# if num == 20:
#     if num2 == 40:
#         print("You got both right!")
#     else:
#         print("You got 2nd wrong.")
# else:
#     print("You got both wrong.")

# ------------------- 09 - Type casting --------------------------
# type casting means conversion
# num = '43'
# num = int(num)
# print(type(num))
# num2 = 687
# num2 = str(num2)
# print(type(num2))   #Regex is used to prevent enterinf alphabets when asked integers and vice versa
# num3 = "43.0"
# num3 = float(num3)
# print(type(num3))

# ------------------- 10 - Multiline string ----------------------
# a = """Hello world, how are you?
# Yes interviewer, I am fine. What about you?"""
# print(type(a), len(a))

# ------------------- 11 - Concatenation -------------------------
# a = "hello"        #Concatenation means to add the strings [combine]
# b = "world"
# c = 32
# d = 534
# print(str(c) + " " + a + " " + str(d) + " " + b)

# -------- 12 - Format in string and integers / float -------------
# marks = 45
# total = "Your total marks is 100 and and you got {}"
# obt = total.format(marks)
# print(obt)
#-----
# age = 22
# total = 100
# obt = 90
# result = "Your age is {1} and your total marks {2} and obtain marks {0}"
# tot = result.format(obt, age, total)      #format ke sequence se 'result' me indexing kry gy!
# print(tot)

# ------------------- 13 - String slicing -------------------------
# a = "hello world"
# print(a[2:6])   #from 2nd index to 5, not 6 [last index does not inculde]
# print(a[-3:-1]) #this will not include the last index
# print(a[-5:])   #to include last digit we will not include the last index
# print(a[-8:-3])

# ------------------- 14 - Split in string ------------------------
# z = "Hello AI class"
# y = z.split(", ")   #by putting a comma, the string will enter into the list but one as a whole
# x = z.split(" ")    #by putting an empty spaces, this will separate all the string elements seperately
# print(z, y, x)       

# --------- 15 - Upper case and lower case in string --------------
# string = "happy birthday!"
# up = string.upper()          #upper case
# lo = string.lower()          #lower case
# ti = string.title()          #title case
# cap = string.capitalize()    #capitalize
# print(f"Upper: {up}, Lower: {lo}, Title: {ti}, Capitalized: {cap}")

# ------------------- 16 - Lists ----------------------------------
# a = 15
# [Karachi | lahore | Peshawer | Multan]
# 0 x 0.012... | 0 x 0...                            --> This is fixed memeory allocated to the list/ram
# 0|1|2|3                                            --> This is an index number which hold the value like what we allocated "a=15"
# ls2 = list(("Lahore", "Seoul", "Edinburgh"))       #this is a constructor method
# # print(ls[2:])
# ls = ["Lahore", "Seoul", "Edinburgh"]                #OR
# ls[1] = "Karachi"        #OR            #in string we can only add/replace/change a single value
# ls[1:] = ["Karacih", "Sydney", "Tokyo"]    #we can replace/add/change more than one value
# print(ls)
# ls[0::3] = ["Mumbai", "Los Angelas"]
# ls.append("Quetta")        #will add the value at the endof the list
# print(ls)
# ls.insert(2,"Seoul")       #will add at the specific index
# print(ls)
# ls.pop(1)                  #will use index number to pop the element from the list if you know the indexes of the list
# print(ls)
# ls.remove("Los Angelas")   #will pass the value directly in order to remove the value from the list if you don't know the indexes of the list but values
# print(ls)
# del ls
# print(ls)                  #this will give an error cuz list "ls" is already deleted
# ls.clear()                 #this will remove all the values but will not the list itself like "[]"
# print(ls)

# ------------------- 17 - Loops ----------------------------------
# ls = ["apple", "banana", "mango"]
# for i in ls:                          
#     print(i)

# ------------------- 18 - For loop while loop --------------------
# ls = ls = ["apple", "banana", "mango"]
# for i in range(len(ls)):
    # print(ls[i], i+1)
# i = 0
# while i < len(ls):
#     print(ls[i])
#     i = i + 1

# ------------------- 19 - Range ----------------------------------
# for i in range(0, 20, 2):
#     print(i)

# ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(ls[1::2])

# ------------------- 20 - List comprehension ---------------------
# minimize the coding length
# ls = [x for x in range(2, 15, 2)]
# print(ls)
# ls = ["lahore", "Islamabad", "Faislabad", "sparrow"]
# ls2 = []
# for i in ls:
#     if "l" in i:
#         ls2.append(i)
# print(ls2)
# SHORT FORM
# ls = ["lahore", "islamabad", "faislabad", "sparrow"]
# ls2 = [x for x in ls if "r" in x] #OR [print(x) for x in ls if "r" in x]
# ls2 = [x for x  in ls if x != "Islamabad"]
# ls2 = [x[0].lower() + x[1:-1].upper() + x[-1:].lower() for x in ls]
# ls2 = [x[0].upper() for x in ls if "F" in x]
# print(ls2)




# ------------------- ASSIGNMENTS -----------------------
# -------------------- CODE # 01 ------------------------
# edu = int(input("Enter your education: "))
# age = int(input("Enter your age: "))
# height = float(input("Enter your height: "))
# if (edu >= 12 and 18<=age<=32):
#     print("Pass")
# elif (edu >= 12 and height >= 5.6):
#     print("Pass")
# elif (height >= 5.6 and 18<=age<=32):
#     print("Pass")
# else:
#     print("Fail")

# -------------------- CODE # 02 ------------------------
# mark1 = float(input("Enter marks 1: "))
# mark2 = float(input("Enter marks 2: "))
# mark3 = float(input("Enter marks 3: "))
# percentage = ((mark1 + mark2 + mark3) / 150) * 100
# print(percentage)

# -------------------- CODE # 03 ------------------------
#bonus after every 6 months 15000
#salary ka 22% bonus he
#find salary?
#22% x salary = 15000
#salary = 15000 / 0.22
#print(int(salary))

# -------------------- CODE # 04 ------------------------
# st = "Jaranwala Faislabad Lahore Karachi Multan"
# print(st.lower())

# -------------------- CODE # 05 ------------------------
#Capitalizing the 1st letters of every element in the list
# cities = ["lahore", "faisalbad", "jaranwala"]
# c = []
# for i in cities:
#     j = i.capitalize()
#     c.append(j)
# print(c)

#Capitalizing the 1st and last letters of every element in the list
# cities = ["lahore", "faisalbad", "jaranwala"]
# c = []
# for i in cities:
#     j = i[0:1].upper() + i[1:-1].lower() + i[-1:].upper()
#     c.append(j)
# print(c)

#OR

# cities = ["lahore", "faisalbad", "jaranwala"]
# c = []
# for i in cities:
#     j = i.capitalize()
#     k = j[:-1] + j[-1:].upper()
#     c.append(k)
# print(c)

#Capitalizing the 2nd and 2nd last letter of every element in the list
# cities = ["lahore", "faisalbad", "jaranwala"]
# c = []
# for i in cities:
#     j = i[0:1].lower() + i[1:2].upper() +i[2:-2].lower() + i[-2:-1].upper() + i[-1:].lower()
#     c.append(j)
# print(c)

#Reversing the list
# cities = ["Washington", "Melbourne", "Lahore", "Faisalbad", "Jaranwala"]
# c = []
# for i in cities:
#     c.insert(0, i)
# print(c)

# cities = ["Washington", "Melbourne", "Lahore", "Faisalbad", "Jaranwala"]
# c = []
# for i in cities:
#     j = i[0:-1]
#     c.append(j)
#     # c.insert(0, i)
# print(c)


# -------------------- CODE # 06 -----------------------
#make 10 cities user input              DONE ✔️
#1st reverse                            DONE ✔️
#1st and last digit capitalize          DONE ✔️
#inbetween letters must be lower case   DONE ✔️


# def print_list(u_l, t):
#     for i in range(t):
#         inp_city = input("Enter the city name: ")
#         u_l.append(inp_city)
#     return u_l

# def reverse_list(u_l, p_l):
#     for i in p_l:
#         u_l.insert(0, i)
#     return u_l

# def f_l_capitalize(u_l, rl):
#     for i in rl:
#         j = i[0:1].upper() + i[1:-1].lower() + i[-1:].upper()
#         u_l.append(j)
#     print(u_l)

# user_list = []
# times = int(input("For how many times you want to enter the cities name: "))
# ls = print_list(user_list, times)
# print(ls)
# user_list = []
# r_ls = reverse_list(user_list, ls)
# user_list = []
# f_l_capitalize(user_list, r_ls)

#OR      (without using functions)

# user_list = []
# times = int(input("For how many times you want to enter the cities name: "))
# for i in range(times):
#     inp_city = input("Enter the city name: ")
#     user_list.append(inp_city)
# print(user_list)
# u_l = []
# for i in user_list:
#     u_l.insert(0, i)
# print(u_l)
# ls = []
# for i in u_l:
#     j = i[0:1].upper() + i[1:-1].lower() + i[-1:].upper()
#     ls.append(j)
# print(ls)

# -------------------- CODE # 07 -----------------------
# for x in range(1, 11):
#     print(f"2 * {x} = {x * 2}")

# [print(f"2 * {x} = {x * 2}") for x in range(1, 11)]
# user_inp = int(input("Enter the range: "))
# ls = [(i**2) for i in range(1, user_inp + 1)]

# -------------------- CODE # 08 -----------------------
# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# # ls = [num1, num2]
# # print(ls)
#OR
# ls = []
# ls.extend([num1, num2])
# print(ls)

# -------------------- CODE # 09 -----------------------
# fact =1
# for i in range(1, 6):
#     fact = fact * i
# print(fact)

# -------------------- CODE # 09 -----------------------
# user_range = int(input("Enter your range: "))
# check = input("What you want to check how many times it came: ")
# count = 0
# listt = []
# for i in range(1, user_range + 1):
#     if check in str(i):
#         count + 1
#         listt.append(i)
# print(count)
# print(listt)
