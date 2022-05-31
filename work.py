"""
x = 2 + 3
y = 8
z = x * y 
"""
#name = "Clement"
#print(z)
#print(name)
#print(type(x))
#print(type(name))
#print(y/x)
#print(type(y/x))
#print(type([5,6]))
#print(type({'a':'john','b':20})) 
"""
def square(x):
    print(x*x)
square(20)
"""
"""
def exponent(x,y):
    print(x**y)
exponent(12,3)
"""
#print(name[:])
#print(len(name))
#scores = [1,2,3,4,5,6,7]
#print(scores[1::2])#prints from the second digit in the list and steps 2 times to print the even numbers.
#print(scores[::2]) #prints from the first digit in the list and steps 2 times to print the odd numbers.

"""
LOOPS.
FOR LOOP
WHILE LOOP.
"""
# x = 0
# while x < 10:
#     print("Clement")#to be printed on the same line, use print("Clement",end='').
#     x = x + 1

# x = 0
# while x < 9:
#     print("clement", end='')
#     x = x + 1

# for x in range(8):
#     print("Hi!", end='')

# y = [1,2,5]
# for x in y:
#     print("hello!")

# def my_sum(x,y):
#     print(x+y)
# my_sum(1012,10012)
    
# def my_sum(x,y):
#     return x+y
# x = my_sum(1012,10012)
# print(x)

# def is_even(x):
#         if x%2 == 0:
#             print("is even")
#         else:
#             print("odd")
# is_even(2.1)
"""
/ -> divides and returns a float like 4.2.
// -> divides and returns an integer without a remainder: if 7//3 will give 3 and not 3.5.
% -> divides and returns a remainder.
"""
# def is_odd(x):
#         if x%2 == 0:
#             return False
#         return True
# is_odd(5)

# ans = False
# def is_even(x):
#         if x%2 == 0:
#             ans = True
#         else:
#             ans = False
#         return ans
"""
In programming, return is used instead of print, because functions are defined to return values which are used to perform tasks. Therefore always replace print with return.
"""
# def is_prime(x):
#     if x%2 != 0 and x/x == 1:
#         return "is prime"
#     else:
#         return "is not prime"
# #is_prime()

"""
CHECK PRIME
"""
# def is_prime(x):
#     first_5 = [2, 3, 5, 7, 11]
#     if x < 12:
#         if x in first_5: 
#             return "prime"
#         return "not prime"
#     for y in first_5:
#         if x % y == 0:
#             return "not prime"
#     return "prime"

# for i in range(20):
#     print(f"{i} is: {is_prime(i)}")
"""
TO SUM A LIST
"""
# def sum_list(x):
#     ans = 0
#     for i in x:
#         ans += i
#     return ans
"""
TO CALCULATE AVERAGE
"""
# def sum_list(x):
#     ans = 0
#     for i in x:
#         ans += i
#     return ans/len(x)
"""
FILE OPERATION
Pseudo code:
check if files exist:
    if true:
        open for reading
    else:
        say, "file does not exist"
        ask if to create file with name ?
"""
# with open('file', 'a') as new_file:
#     new_file.write("Here comes a new file")

# f = open('new_file', 'a')
# f.write('\nThis is a new paragraph')
# print("")
# f.close()

# with open('new_file', 'r') as f:
#     text = f.read()
#     print(text)

file_name = input("Enter file name.\n")
if file_name:  #this is same as file_name != "" '
    new_text = input(f"Enter text to be stored in {file_name} and press enter:\n")

    f = open(file_name, 'a')
    f.write('new_text')
    print("")
    f.close()

    with open(file_name, 'r') as f:
        text = f.read()
        print(f"Text in {file_name} has {len(text)} characters in it.\n Here is the text itself:\n {new_text}")
else:
    print("Please enter a valid file name")
