# ---------------------- 28. File Handling ----------------------
# file = open("G:/Course/Week#03/xtfile.txt", "r")        #this for only read the file [we need to use forward slash or double back slash]
# print(file.read())                                      #this will only print whole file
# print(file.read(10))                                    #if we will pass value in read function, it will print character to that index
# print(file.readline())                                  #print only 1st line
# print(file.readline())                                  #passing same print, it will print line by line
# for i in file:                                          #or we can use for loop to print line by line
#     if "File" in i:
#         print("Yes!")
#     else:
#         print("No!")
# file.close()                                            #file closed
# choice = input("""What you want to do with the file:
#                a. Append the file
#                r. read he file
#                w. write the file
#                 """)
# if choice == "a":
#     file = open("G:/Course/Week#03/xtfile.txt", "a")
#     file.write("This is another line added ny fil handling.")
# else:
#     print("whatver")

st = "hello class of all!"
# st = st.title()
# strr = st.split(" ")

#OR

strr = st.split(" ")
ky[print(i[0].upper() + i[1:].lower()) for i in strr]