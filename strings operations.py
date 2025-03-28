#concatination of two/three strings.
s='sanjay'
v='vitthal'
y='yedage'
sanjay=s+""+v+""+y
print(sanjay)
print(s+v+y)

#length of string.
print(len(sanjay))

#string slicing.
print(s[0:3])

#string ends with().
str="i am coder."
print(str.endswith("coder."))
print(str.endswith("am"))

#string capitalize().
print(str.capitalize())

#string replace().
print(str.replace("code","sanjay"))
print(str.replace("r","s"))

#string find().
print(str.find("am"))

#string count().
print(str.count("am"))

name=input("Enter your name:")
print(len(name))
