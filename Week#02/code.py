# ------------------- 21 - Tuples -----------------------
# To change the values in tuples, we need to convert it into list first then back to tuple
# tp = tuple(("Hello", "world"))
# ls = list(tp)
# ls.append("guru99")
# print(tuple(ls))

# tup1 = ("tup1",)
# tup2 = ("tup2",)
# tup3 = tup1 + tup2
# print(tup3)

# tt = ("lahore", "islamad", "london")
# ls = list(tt)
# ls1 = []
# for i in ls:
#     abc = i[0].upper() + i[1:].lower()
#     ls1.append(abc)
# print(tuple(ls1))

# tup = ("School", "College", "University")
# (tup1, tup2, tup3) = tup                     #UNPACKING
# print(tup3)

# tup = ("Born", "Live", "Learn", "School", "College", "University", "Masters", "Job", "Retired", "Death")
# (tup1, tup2, *tup3, tup4, tup5) = tup        #'*' Asteric
# print(tup3)                                  #Will print first 4 values with tup1, tup2, tup3, tup4 and in tup 5 all the remaining list will get printed

# tup = ("Born", "Live", "Learn", "School", "College", "University", "Masters", "Job", "Retired", "Death")
# (tup1, tup2, tup3, *tup4, tup5) = tup          #Index 2 to 3rd last will be packed      
# print(tup4)

# ------------------- 22 - Sets -----------------------
# Will remove repeated words
# st = {"git", "github", "vscode", "turbo c++", "vscode"}
# print(st)

# st = set(("git", "github", "vscode", "turbo c++", "anaconda"))
# st2 = set(("pycharm", "notpad++", "thonny"))
# st.add("IDE")            #will take only one argument
# st.update(st2)           #this will update st and join st2 with it
# st.pop()                 #will pop random value
# st.remove("git")         #will remove that value
# print(st)

# st = set(("git", "github", "vscode", "turbo c++", "anaconda", 0, 1, "yes", "no", True, False,))
# # If True-False will enter into the list, then it will print in the set not 0-1
# print(st)

# st = set(("git", 59, "github", "vscode", 99, 42, "turbo c++", "anaconda", "yes", "no"))
# st.remove("yes")
# print(st)
# st.discard("github")
# print(st)
# st.clear()
# print(st)
# del st
# print(st)

# st1 = {"so", "yeah!", "cisco"}
# st2 = {"what?", "cisco", "who?"}
# st4 = {"so", "yeah!", "this", "aha!"}
# st3 = st1 | st2                              #in sets bar "|" means adding (to use if we have multiple sets) or we can use union
# print(st3)
# st3 = st1.union(st2) | st4
# st5 = st1.intersection(st2)
# st5 = st1 & st2                               #in sets and "&" means intersection (to use if we have multiple sets) or we can use union
# st5 = st2.difference(st1)                      #in sets difference "-" means the same values in both set will be removed from 1st set
# print(st5)

# ------------------- 23 - Dictionaries --------------------
# dic = dict({"name":"amna","age":22})             #we have to put curly brackets not round
# print(type(dic), dic, len(dic))                  #sirf sets or dict ko hum round ke andr curly braces use kry gy jab keh list or tuples mein hum double round braces bhi laga saktein hein

# print(dic["name"])                #OR
# print(dic.get("age"))             #this is READING the data
# dic["name"] = "bushra"            #OR
# print(dic.get("name"))
# dic["city"] = "Changa Manga"
# dic.update({"city":"Kahna Nau", "color":"light brown"})
# dic.clear()        #will clear all the items of the list
# dic.pop("city")    #will remove specific key/pair
# dic.popitem()
# print(f"Dictionary keys: {dic.keys()} - Dictionary values: {dic.values()}")
# print(dic.items())
# del dic["city"]
# del dic
# print(dic)

# dic = {
#     "name":"zahid",
#     "age":23,
#     "fruits":{
#         "brand1":"Dior",
#         "brand2":"LV"
#         }}
# print(dic)
# dic.update({"fruits":{"fruits1":"apple"}, "vegetables":{"veg1":"potato"}})
# print(dic)
# dic.pop("fruits")
# print(dic)


# QUESTION, USER DICTIONARY


# ------------------- 24 - Pass by reference / Pass by value -------------
# Pass by value - Primitive data types
# a =10
# b = a
# a =20
# print(a ,b)

# Pass by reference - NonPrimitive data types - Shallow copy
# dic1 = {"name":"amna", "age":22}
# dic2 = {"name":"amna", "age":22}
# # dic2 = dic1
# # dic1["name"] = "adil"
# # print(dic1,dic2)
# # dic2 = dic1.copy()           #this will not copy the address
# dic1["name"] = "shabanna"
# print(dic1, dic2)

# ------------------- 25 - FUNCTIONS ---------------------------------------
# def s():
#     print("Whats up man!")
# s()

# def func(name, age):           #if we put pass the value with a parameter again then it will get overwrite with the value pass in the function
#     print("Hello World", name, age)
# func("Irbaz", 22)

# def func(name = "Karamat", age = 60):        # if we gave one default parameter then we have to give default values to all the rest of the variable in the function as well
#     print("Hello World", name, age)
# func("Irbaz", 22)
# func()

# def func(name, *age):
#     print("Hello World" + " " + name + " " + str(age[2]))  #we can call using indexing
# func("Irbaz", 22, 234, 5353)        #all the values will be entered into the asteric

# def fun(**kwargs):
#     print(kwargs["name"] + " " + str(kwargs["age"]))
# fun(name = "Irbaz", age = 22)

# def fun():
#     pass
# fun()

# ------------------- 26 - Exception Hnadling ------------------------
# X = 23
# try:
#     print(f"X is {X}")
# except:
#     print("ERROR BITCH")
# finally:
#     print("I AM IDIOT! I WILL STILL RUN B@STARDS")

# ------------------- 27 - Anonymous Function -------------------
# x = lambda a, b, c:a * (b / c)      #in Lambda return is built-in
# print(x(2, 4, 2))


# CODE 01
# st = {"Rabia Saleem", "Imran Khan", "Zubbair"}
# print(st)
# st1, st2, st3 = st
# st1 = "Nicholas Galetzine"
# st2 = "Louis Partridge"
# st3 = "Margret Stuwart"
# st = st1, st2, st3
# lst = list(st)
# print(lst)
# print(tuple(lst))

#CODE 02
# ls = ["copy", "pencil", "marker"]
# tup = ("bus", "car", "bike")
# tupp = list(tup)
# st1 = ls + tupp
# set1 = set(st1)
# set2 = set(tup)
# print("Difference: ",set1 - set2)
# print("Union: ", set1.union(set2))
# print("Intersection: ", set1.intersection(set2))

#CODE 03
# tup = ("Addidas", "Bata", "Gucci", "Servis", "'Dior", "Chanel","LV","Stylo", "Outfitters", "Nike")
# (tup1, tup2, tup3, tup4,tup5,tup6, tup7, tup8, *tup9) = tup
# print (tup9)
# ls = tup9 + ["Roma", "Dell", "HP"]
# print(set(ls))



# ------------------- MIT -------------------------------
#01. Primitive data types = Pass by value [Aek value ke change hony se doosri value channge nahi ho gi 'different addresses]
#02. Non-Primitive data types = Pass by Reference [Aek value ke change hony se doosri value channge ho gi automatically  'same addresses] [list, tuples, dict]
#03. Deep copy and shallow copy difference
#04. Primitive and Non-Primitive data types difference [change depends on data types]
#05. Packing and Unpacking
#06. '*' Asteric can be used in tuples - lists or dict
#07. List constructor always done in double parenthesis like = list((23,455,66)) or set(("Hi","Bye"))
#08. Arguments mean adding values and parameters means adding variables
#09. API
#10. Shallow Copy & Deep Copy [this will change the values even in the nested dic-list-tuple]
#11. CRUD - Create Read Update Delete
#12. Kivi android apps library
#13. tkinter is also a library, UI library
#14. C# is used for desktop application
#15. APK stands for Application Package Kit + iOS stands for 
#16. Single asteric (*) means arbitrary arguments [We pick indexes and work with them] and double asteric (**) means kwargs [we work with dictionaries in it]
#17. Ruturn will push to the server and also will print it to the user.