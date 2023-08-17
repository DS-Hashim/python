spam_amount = 0
print(spam_amount)

# Ordering Spam, egg, Spam, Spam, bacon and Spam (4 more servings of Spam)
spam_amount = spam_amount + 4

if spam_amount > 0:
    print("But I don't want ANY spam!")

viking_song = "Spam " * spam_amount
print(viking_song)


### Numbers and arithmetic in Python

spam_amount = 0

type(spam_amount)

type(19.95)

print(5 / 2)
print(6 / 2)

print(5 // 2)
print(6 // 2)

hat_height_cm = 25
my_height_cm = 190
# How tall am I, in meters, when wearing my hat?
total_height_meters = hat_height_cm + my_height_cm / 100
print("Height in meters =", total_height_meters, "?")

total_height_meters = (hat_height_cm + my_height_cm) / 100
print("Height in meters =", total_height_meters)

# Builtin functions for working with numbers

print(min(1, 2, 3))
print(max(1, 2, 3))

# abs returns the absolute value of an argument:

print(abs(32))
print(abs(-32))

# In addition to being the names of Python's two main numerical types, int and float can also
# be called as functions which convert their arguments to the corresponding type:

print(float(10))
print(int(3.33))
# They can even be called on strings!
print(int('807') + 1)

print(-a(1))



def least_difference(1, 10, 100):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    reture min(diff1, diff2, diff3)

print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7), # Python allows trailing commas in argument lists. How nice is that?


