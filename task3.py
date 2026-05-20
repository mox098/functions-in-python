# 1) Define a function `add(P, Q)` that returns the sum of two numbers (P + Q).
def add(p,q):
    return p+q
# 2) Define a function `subtract(P, Q)` that returns the difference of two numbers (P - Q).
def sub(p,q):
    return p-q
# 3) Define a function `multiply(P, Q)` that returns the product of two numbers (P * Q).
def multiply(p,q):
    return p * q
# 4) Define a function `divide(P, Q)` that returns the division result of two numbers (P / Q).
def div(p,q):
    p/q 
# 5) Display a menu to the user showing the available operations:
print("what is your choice a)add b)subtract c)mutliply d)divide")
# a) Add

# b) Subtract

# c) Multiply

# d) Divide

# 6) Take the user's choice as input and store it in `choice`.
choice=(input("enter a choice"))
# 7) Take two integer inputs from the user:

# a) Store the first number in `num_1`
num1=int(input("enter a number"))
# b) Store the second number in `num_2`
num2=int(input("enter a number"))
# 8) Use conditional statements to perform the chosen operation:

# a) If `choice` is 'a', call `add(num_1, num_2)` and print the result.
if choice=="a":
    print(add(num1,num2))
elif choice=="b":
    print(sub(num1,num2))
elif choice=="c":
    print(multiply(num1,num2))
elif choice=="d":
    print(div(num1,num2))
else:
    print("invalid input!")





# b) Else if `choice` is 'b', call `subtract(num_1, num_2)` and print the result.

# c) Else if `choice` is 'c', call `multiply(num_1, num_2)` and print the result.

# d) Else if `choice` is 'd', call `divide(num_1, num_2)` and print the result.

# 9) If the user enters anything other than a/b/c/d, print an invalid input message.