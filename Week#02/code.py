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

# tt = ("lahore", "islamad", "london")
# tt1 = (1, 2, 3, 4)
# tup3 = tt1 + tt
# tup3 = tup3[4:] + tup3[:4]
# print(tup3)

tt = ["lahore", "islamad", "london"]
print(list(tt))

# tt1 = (1, 2, 3, 4)
# tup3 = tt1 + tt
# ls = list(tup3)
# ls2 = []
# for i in ls:
#     ls2.insert(0, i)
# print(ls2)
# tup4 = tuple(ls2)
# print(tup4)

#ASSIGNMENT
#5 methods

# ------------------- MIT -------------------------------
#01. Primitive data types = Pass by value [Aek value ke change hony se doosri value channge nahi ho gi 'different addresses]
#02. Non-Primitive data types = Pass by Reference [Aek value ke change hony se doosri value channge ho gi automatically  'same addresses] [list, tuples, dict]
#03. Deep copy and shallow copy difference
#04. Primitive and Non-Primitive data types difference [change depends on data types]