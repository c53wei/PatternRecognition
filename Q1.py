# Question One: Python Syntax Warmup
# Note: It should be easy to get these right, but be sure to check the correctness of your answers
# by running your code and printing the result.
# a) Write a Python statement that generates a vector with values from 10 to 20 in steps of 2,
# and assigns it to the variable ‘x’.
x = list(range(10, 21, 2))

# b) Write code that creates a variable called ‘total’, sets it to zero, and adds the elements of x
# to total using a for loop.
total = 0
for val in x:
    total+=val

# c) Put the code from (b) in a function called ‘find_total’, which takes a list x as a parameter,
# and returns total.
def find_total(x: list) -> int:
    total = 0
    for val in x:
        total+=val
    return total
# d) Write a Python expression that returns the second through fourth elements of x. Remember
# the elements are indexed from zero.
print(x[1:4])