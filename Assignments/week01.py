# ------------------- ASSIGNMENTS -----------------------
# -------------------- CODE # 01 ------------------------
edu = int(input("Enter your education: "))
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
if (edu >= 12 and 18<=age<=32):
    print("Pass")
elif (edu >= 12 and height >= 5.6):
    print("Pass")
elif (height >= 5.6 and 18<=age<=32):
    print("Pass")
else:
    print("Fail")

# -------------------- CODE # 02 ------------------------
mark1 = float(input("Enter marks 1: "))
mark2 = float(input("Enter marks 2: "))
mark3 = float(input("Enter marks 3: "))
percentage = ((mark1 + mark2 + mark3) / 150) * 100
print(percentage)

# -------------------- CODE # 03 ------------------------
# bonus after every 6 months 15000
# salary ka 22% bonus he
# find salary?
# 22% x salary = 15000
salary = 15000 / 0.22
print(int(salary))

# -------------------- CODE # 04 ------------------------
st = "Jaranwala Faislabad Lahore Karachi Multan"
print(st.lower())

# -------------------- CODE # 05 ------------------------
# Capitalizing the 1st letters of every element in the list
cities = ["lahore", "faisalbad", "jaranwala"]
c = []
for i in cities:
    j = i.capitalize()
    c.append(j)
print(c)

# Capitalizing the 1st and last letters of every element in the list
cities = ["lahore", "faisalbad", "jaranwala"]
c = []
for i in cities:
    j = i[0:1].upper() + i[1:-1].lower() + i[-1:].upper()
    c.append(j)
print(c)

# OR

cities = ["lahore", "faisalbad", "jaranwala"]
c = []
for i in cities:
    j = i.capitalize()
    k = j[:-1] + j[-1:].upper()
    c.append(k)
print(c)

# Capitalizing the 2nd and 2nd last letter of every element in the list
cities = ["lahore", "faisalbad", "jaranwala"]
c = []
for i in cities:
    j = i[0:1].lower() + i[1:2].upper() +i[2:-2].lower() + i[-2:-1].upper() + i[-1:].lower()
    c.append(j)
print(c)

# Reversing the list
cities = ["Washington", "Melbourne", "Lahore", "Faisalbad", "Jaranwala"]
c = []
for i in cities:
    c.insert(0, i)
print(c)

cities = ["Washington", "Melbourne", "Lahore", "Faisalbad", "Jaranwala"]
c = []
for i in cities:
    j = i[0:-1]
    c.append(j)
    # c.insert(0, i)
print(c)


# -------------------- CODE # 06 -----------------------
# make 10 cities user input              DONE ✔️
# 1st reverse                            DONE ✔️
# 1st and last digit capitalize          DONE ✔️
# inbetween letters must be lower case   DONE ✔️


def print_list(u_l, t):
    for i in range(t):
        inp_city = input("Enter the city name: ")
        u_l.append(inp_city)
    return u_l

def reverse_list(u_l, p_l):
    for i in p_l:
        u_l.insert(0, i)
    return u_l

def f_l_capitalize(u_l, rl):
    for i in rl:
        j = i[0:1].upper() + i[1:-1].lower() + i[-1:].upper()
        u_l.append(j)
    print(u_l)

user_list = []
times = int(input("For how many times you want to enter the cities name: "))
ls = print_list(user_list, times)
print(ls)
user_list = []
r_ls = reverse_list(user_list, ls)
user_list = []
f_l_capitalize(user_list, r_ls)

# OR      (without using functions)

user_list = []
times = int(input("For how many times you want to enter the cities name: "))
for i in range(times):
    inp_city = input("Enter the city name: ")
    user_list.append(inp_city)
print(user_list)
u_l = []
for i in user_list:
    u_l.insert(0, i)
print(u_l)
ls = []
for i in u_l:
    j = i[0:1].upper() + i[1:-1].lower() + i[-1:].upper()
    ls.append(j)
print(ls)

# -------------------- CODE # 07 -----------------------
for x in range(1, 11):
    print(f"2 * {x} = {x * 2}")

[print(f"2 * {x} = {x * 2}") for x in range(1, 11)]
user_inp = int(input("Enter the range: "))
ls = [(i**2) for i in range(1, user_inp + 1)]

# -------------------- CODE # 08 -----------------------
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
# ls = [num1, num2]
# print(ls)
# OR
ls = []
ls.extend([num1, num2])
print(ls)

# -------------------- CODE # 09 -----------------------
fact =1
for i in range(1, 6):
    fact = fact * i
print(fact)

# -------------------- CODE # 09 -----------------------
user_range = int(input("Enter your range: "))
check = input("What you want to check how many times it came: ")
count = 0
listt = []
for i in range(1, user_range + 1):
    if check in str(i):
        count + 1
        listt.append(i)
print(count)
print(listt)

# -------------------- CODE # 10 -----------------------
# LIST COMPREHENSION                                          DONE ✔️
# USING LIST SLICING AND UNDERSTANDING [-1:-1] STUFF          DONE ✔️
# GIT COMMANDS                                                DONE ✔️
# TUPLE IDEA                                                  DONE ✔️

values = int(input("How many values you want to enter: "))
user_list = []
for i in range(values):
    value = int(input(f"Enter value {i+1}: "))
    user_list.append(value)
print([(x**2) for x in user_list])

ls = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print([x for x in ls if x % 2 == 0])

str = input("Enter string: ")
print([char for char in str if char.lower() in {"a", "e", "i", "o","u"}])

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
print([x for x in list if x % 3 == 0 or x % 5 == 0])

ls = ["apple", "banana", "cherry", "date"]
print([len(i) for i in ls])

ls = [5, -2, 10, -8, 0, 3]
print([x for x in ls if x >= 0])

w = "hello-world"
print(w[::-2])