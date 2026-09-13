# 1. Python Basics & Setup question
# 1. Write a Python program that prints Hello, World!.
print("Hello, World!")
# 2. Print your name, age, college, and city on separate lines.
name = "ridhi"
age = 18
college = "IITM COLLEGE"
city = "DELHI"
print(name)
print(age)
print(college)
print(city)
# 3. Print a sentence using escape sequences for a new line and a tab.
print("hello!!!\nMy self Ridhi\tMy age is 20")
# 4. Display the result of 15 + 27.
print(15+27)
# 5. Display the result of 100 - 38.
print(100-38)
# 6. Display the result of 12 * 9.
print(12*9)
# 7. Display the result of 144 / 12.
print(144/12)
# 8. Display quotient and remainder when 29 is divided by 5.
print(29//5,29%5)
# 9. Write a program that prints the square and cube of a number.
num1 = 8
print(pow(num1,2))
print(pow(num1,3))
# 10. Write a program that prints a simple ASCII art pattern using print().
print("--------------------")
print("|     O     O      |")
print("|        @         |")
print("|    --------      |")
print("|                  |")
print("--------------------")
# 11. Use comments to explain a small Python program.
# This program prints a statement
print("Hello")

# This performs addition
print(10 + 20)
# 12. Show the difference between single, double, and triple quoted strings with examples.
single = 'hello,\"ridhi this side"'
print(single)
double ="hello,\"ridhi this side"
print(double)
triple ="""Hello
"ridhi this side"
how are you？"""
print(triple)
# 13. Write a program that prints a formatted receipt using print().
price1 = 90
price2 = 100
price3 = 140
print("=========Receipt=========")
print(f"Pasta ${price1}")
print(f"pav bhaji ${price2}")
print(f"Cake ${price3}")
print("=========================")
print(f"Total amount ${price1+price2+price3}")
print("=========================")
# 14. Use sep and end arguments in print() 
print("Apple","cherry","Mango",sep=",")
print("lady",end="-")
print("finger")
# 15. Create a program that displays a three-line menu.
menu ="""=============Menu============
     food                price
     1.pasta              $70
     2.pizza              $120
     3.finger             $50
  =============================="""
print(menu)
# 16. Write a program that prints a multiplication table for 7.
print(7*1)
print(7*2)
print(7*3)
print(7*4)
print(7*5)
print(7*6)
print(7*7)
print(7*8)
print(7*9)
print(7*10)
# 17. Print numbers from 1 to 10 without using a loop.
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)
# 18. Create a program that demonstrates Python's indentation rule.
condition = False
if condition:
    print("this will not excute")
print("this will excute")
# 19. Write a program that intentionally causes an indentation error, then correct it.
condition1 = True
if condition1:
# print("indentation error")
    print("right way to do")

# 20. Find the Python version at runtime using Python code.
'''step1: open terminal in vscode
step2: type python --version or py --version
step3: press enter'''
import sys

print(sys.version)