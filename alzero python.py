# # a = "I Love Python"
# # print(len(a))

# # print(" i dont what the fuck im doing ")

# a = "I Love Python"
# print(a.split())

# b = "I-Love-Python"
# print(b.split())

# c = "I-Love-Python"
# print(c.split("-"))

# d = "I-Love-Python-and-R"
# print(d.split("-", 2))


# # center()

# e = "Hashim"
# print(e.center(10))       #spaces
# print(e.center(10, "$"))     #Hashes


# # count()

# f = "I Love Python and R Because R is Easy"
# print(f.count("R")) # 2 R 
# print(f.count("R", 0, 20))  # Only 1 R

# # sawpcase()

# g = "I Love Python"
# h = "i lOVE pYThon"

# print(g.swapcase())
# print(h.swapcase())


# # startswith()

# i = "I Love Python"
# print(i.startswith("I"))


# index (SubString, Start, End)

# a = "I Love Pyhton "
# print(a.index("P")) # index number 7

# replace (Old Value, New Value, Count)

# a = "Hello One Two Three One One"
# print(a.replace("One", "1"))

# print(a.replace("One", "1", 1))


# print(a.replace("One", "1", 2))

# # join(iterable)

# myList = ["Hashim", "Mohammed", "Nasser"]
# print(" ".join(myList))




# ----------------------------
# ---- Strings Formating -----
# ----------------------------

Name = "Hashim"
Age = 29
rank = 10.0

print("My Name is: " + Name)
# print("My Name is: " + name + "and My Age is: " + age)  # Type Error

print("My Name is: %s" % "Hashim")
print("My Name is: %s and My Age is: %d and My rank is: %f" % (Name, Age, rank))

# %s => String
# %d => Number, intr
# %f => Float