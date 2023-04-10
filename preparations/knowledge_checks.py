# Palindrome

check_input = "madam"

org_input = check_input

assert str(org_input) == str(check_input)[::-1]

# Amstrong Number

ams_no = 371

org_ams_no = ams_no

str_arm_no = str(ams_no)

check_arm_no = 0

for i in str_arm_no:
    check_arm_no += int(i) ** 3

assert check_arm_no == org_ams_no


# Generators
def printresult(String):
    for i in String:
        yield i


obj = printresult("Happy")
print(next(obj))
print(next(obj))
print(next(obj))


# Print Pattern
# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern triangle
def triangle(n):
    # number of spaces
    k = n - 1

    # outer loop to handle number of rows
    for i in range(0, n):

        # inner loop to handle number spaces
        # values changing acc. to requirement
        # for j in range(0, k):
        #     print(end=" ")

        # # decrementing k after each loop
        # k = k - 1

        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, k):
            # printing stars
            print("* ", end="")

        # ending line after each row
        print("\r")

        k -= 1


# Driver Code
n = 5
triangle(n)


#  Decorators

# defining a decorator
def hello_decorator(func):
    # inner1 is a Wrapper function in
    # which the argument is called

    # inner function can access the outer local
    # functions like in this case "func"
    def executer():
        print("Hello, this is before function execution")

        # calling the actual function now
        # inside the wrapper function.
        func()

        print("This is after function execution")

    return executer


# defining a function, to be called inside wrapper
def function_to_be_used():
    print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behaviour
function_to_be_used = hello_decorator(function_to_be_used)

# calling the function
function_to_be_used()

# importing libraries
import time
import math


# decorator to calculate duration
# taken by any function.
def calculate_time(func):
    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def inner(*args, **kwargs):
        # storing time before function execution
        begin = time.time()

        func(*args, **kwargs)

        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)

    return inner


# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num):
    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    time.sleep(2)
    print(math.factorial(num))

def sum(a, b):
    time.sleep(2)
    print("Sum of number: {}".format(a+b))

# calling the function.
factorial(10)

sum = calculate_time(sum)
sum(2, 3)


def hello_decorator(func):
    def inner1(*args, **kwargs):
        print("before Execution")

        # getting the returned value
        returned_value = func(*args, **kwargs)
        print("after Execution")

        # returning the value to the original frame
        return returned_value

    return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b


a, b = 1, 2

# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))


# code for testing decorator chaining
def decor1(func):
	def inner():
		x = func()
		return x * x
	return inner

def decor(func):
	def inner():
		x = func()
		return 2 * x
	return inner

@decor1
@decor
def num():
	return 10

print(num())
