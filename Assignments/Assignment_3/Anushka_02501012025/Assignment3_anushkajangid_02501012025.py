# first 10 naturl no
def print_natural():
    for i in range(1, 11):
        print(i)

print_natural()

# sum of first n natural numbers
def sum_natural(n):
    return n * (n + 1) // 2

n = int(input("Enter N: "))
print("Sum =", sum_natural(n))

# reverse
def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    return rev

num = int(input("Enter a number: "))
print("Reverse =", reverse_number(num))

# count digist in num 
def count_digits(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count

num = int(input("Enter a number: "))
print("Digits =", count_digits(num))

# plaindrome
def palindrome(num):
    original = num
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10

    return original == rev

num = int(input("Enter a number: "))
if palindrome(num):
    print("Palindrome")
else:
    print("Not Palindrome")

# fibonaaco
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter number of terms: "))
fibonacci(n)

#calculator
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero not allowed"
    return a / b

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter choice: "))

if choice == 1:
    print("Result =", add(a, b))
elif choice == 2:
    print("Result =", subtract(a, b))
elif choice == 3:
    print("Result =", multiply(a, b))
elif choice == 4:
    print("Result =", divide(a, b))
else:
    print("Invalid Choice")

#Text File and Store Student Details
with open("student.txt", "w") as file:
    name = input("Enter Name: ")
    roll = input("Enter Roll No: ")

    file.write("Name: " + name + "\n")
    file.write("Roll No: " + roll)

print("Student details saved.")

#Read Data From a File
with open("student.txt", "r") as file:
    data = file.read()

print(data)

#Handle Division by Zero Using Exception Handling
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Result =", result)

except ZeroDivisionError:
    print("Cannot divide by zero")

#Handle Division by Zero
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Result =", result)

except ZeroDivisionError:
    print("Cannot divide by zero")

#Student Class with Name and Marks
# class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

s1 = Student("Anushka", 95)
s1.display()        
