#####creating a string

# a = "Divya"
# b = "Sharma"

# print(a)
# print(b)

#####multiline string

# a = "hello world!!,welcome"
# print(a)
# b = "hello my name is divya"
# print(b)

#####accessing characters

# a = [1,2,3,4,5]
# print(a[0])
# print(a[4])

###negative index

# a = [1,2,3,4,5]
# print(a[-1])
# print(a[-4])

####slicing

# a = [1,2,3,4,5,6,7,8,9]
# print(a[0])
# print(a[5])
# print(a[0:])
# print(a[:7])
# print(a[1:6])
# print(a[-4:-1])
# print(a[-7])
# print(a[-9:-1])


####looping through strings

# a = "ABCDEFGH"
# for char in a:
#     print(char)

####immutability-----string are immutable they cannot be changed

# s = "aBCDEF"
# s = "A" + s[1:]  
# print(s)

#####deleting a string

# a = "ABCDE"
# del a

####updating a string

# s = "ABCD EF"
# print(s)
# s1 = "H" + s[1:]
# print(s1)
# s2 = s.replace("ABC","abc")
# print(s2)

####common string method----len of a string

# a = "DivyaSharma"
# print(len(a))

#####upper case and lower case

a = "divya sharma"
print(a.upper())
print(a.lower())

####strip method
a = "  divya sharma  "
print(a.strip())