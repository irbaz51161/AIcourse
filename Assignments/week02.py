# ASSIGNMENT
# 5 methods
# METHOD # 01
tt = ("lahore", "islamad", "london")
tt1 = (1, 2, 3, 4)
tup3 = tt1 + tt
tup3 = tup3[4:] + tup3[:4]
print(tup3)

# METHOD # 02
tt = ("lahore", "islamad", "london")
tt1 = (1, 2, 3, 4)
tup3 = tt1 + tt
ls = list(tup3)
ls2 = []
for i in ls:
    ls2.insert(0, i)
print(ls2)
tup4 = tuple(ls2)
print(tup4)

# Method # 03
tt = ("lahore", "islamad", "london")
tt1 = (1, 2, 3, 4)
tup = tt1 + tt

# SET1 + SET2 + SET3 + SET4
# Join all of em using Union
# Simple convert into List then Tuple

set1 = {"Addidas", "Bata", "Gucci", "Servis"}
set2 = {"copy", "pencil", "marker", "what?", "cisco", "who?"}
set3 = {"Dior", "Chanel","LV","Stylo", "Outfitters", "Nike"}
set4 = {"HP", "Dell", "Mac", "Azure", "Chromebook", "Lenovo"}
main_set = set1 | set2 | set3 | set4        #adding all sets using union 
print(main_set)
ls = list(main_set)
print(ls)
tup = tuple(ls)
print(tup)

def inpp(ls):
    user_city = input("Enter the city name: ").capitalize()
    return ls, user_city
def compare(ls, u_c):
    if u_c in ls:
        print(f"{u_c} is Clean!")
    else:
        print(f"{u_c} is not Clean!")

ls = ["London", "Texas", "Los Angelas", "Belgium","Taxi"]
ls, user_city = inpp(ls)
compare(ls, user_city)

def fun(c):
    alp = False
    ls = ["London", "Texas", "Los Angelas", "Belgium","Taxi"]
    for city in ls:
        if city == c:
            alp = True
    if(alp):
        print("Your city is clean!")
    else:
        print("YOur city is not clean!")
    
c = input("Enter your city name: ")
fun(c)

value = int(input("How many values: "))
num = int(input("Which table you want to print: "))
count = 1
for i in range(1, value+1):
    # table = num * i
    print(num, "X" , i, "=", num * i)

dic = {}     #"name":, "cnic": "", "age": "", "city":""
for info in range(2):
    dic["name"] = input("Enter Name: ")
    dic["cnic"] = input("Enter CNIC: ")
    dic["age"] = input("Enter age: ")
    dic["city"] = input("Enter your city name: ")

print(dic)

def checker(n):
    flagg = False
    if n == 500:
        flagg = True
    print(f"Your number {n} is {flagg}")

num = 50 + 70 - 20 * 2 / 5
checker(num)