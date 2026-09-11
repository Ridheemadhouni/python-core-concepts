# 26. Convert an integer to float and display both values.
price1 = 29
print(price1,type(price1))
price2 = float(price1)
print(price2,type(price2))
# 27. Convert a float to int and observe the result.
rate =9.8888
print(f"In float {rate} In int {int(rate)}")
# 28. Convert an integer to a string and concatenate it with text.
age = 20
Myself = "Hello everyone, My name is ridhi, my age is "+str(age)
print(Myself)
print(f"Hello everyone, My name is ridhi, my age is {age}")
# 29. Take two numbers as input and display their sum.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"Sum of two number: {num2+num1}")
# 30. Take a user's name and age as input and display a sentence.
username = input("Enter your name: ")
userage = int(input("Enter your age: "))
print(f"Your name :{username} Your age :{userage}")
# 31. Calculate simple interest from principal, rate, and time.
p = int(input("enter principle: "))
rate = int(input("Enter rate: "))
time = int(input("enter time: "))
si = (p*rate*time)/100
print(f"Simple interest : {si}")
# 32. Calculate the area and perimeter of a rectangle.
length = int(input("Enter lenght: "))
width = int(input("Enter width: "))
print(f"Area of rectangle {length*width} perimeter of rectangle {2(length+width)}")
# 33. Calculate the area and circumference of a circle.
import math
radius = float(input("Enter radius: "))
print(f"area of circle {math.pi*(radius ** 2)} circumference of circle {2*math.pi*radius}")
# 34. Convert Celsius to Fahrenheit.
temp1 = float(input("Enter temperature: "))

# 35. Convert Fahrenheit to Celsius.
# 36. Convert kilometers to miles.
# 37. Convert seconds into hours, minutes, and seconds.
# 38. Calculate total and average marks for five subjects.
marks1 = float(input("Enter 1st marks: "))
marks2 = float(input("Enter 2nd marks: "))
marks3 = float(input("Enter 3rd marks: "))
marks4 = float(input("Enter 4th marks: "))
marks5 = float(input("Enter 5th marks: "))
total_marks = marks1+marks2+marks3+marks4+marks5
print(f"Total marks: {total_marks} average: {total_marks/5}")
# 39. Calculate percentage from obtained and maximum marks.
m1 = float(input("Enter marks: "))
m2 = float(input("Enter marks: "))
m3 = float(input("Enter marks: "))
m4 = float(input("Enter marks: "))
m5 = float(input("Enter marks: "))
total = m1+m2+m3+m4+m5
print(f"Precentage: {(total/500)*100}")
# 40. Use type() and isinstance() to check variable types.
a = 0
b =8.9
print(f"{type(a)} {isinstance(a)} {type(a)} {isinstance(b)}")
# 41. Use input() safely when the user enters numeric data.
roll_no = int(input("Enter your roll number: "))
# 42. Demonstrate implicit type conversion in arithmetic.
n1 = 4
n2 = 6.7
print(f"Sum {n1+n2}")
# 43. Demonstrate explicit type conversion with int(), float(), and str().
number = 4
number1 = int(number)
Number2 = "30"
Number3 = int(Number2)
print(f"{number} {type(number)}\n{number1} {type(number1)}\n{Number2} {type(Number2)}\n{Number3} {type(Number3)}")
# 44. Create constants using naming conventions and explain why Python does not enforce constants.
key = 1234
key = 4567
print(key)
# 45. Write a program that reports the memory identity of two variables using id().
password = 34
print("Password location",id(password))