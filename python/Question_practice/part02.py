# 2. Variables, Data Types & Type Conversion question
# 21. Create variables for name, age, height, and student status and print their values.
name = 'ridhima'
age = 20
height = 5.2
Status = "A garde"
print(f"Student detail \nname {name} \nage {age} \nheight {height} \nstatus {height}")
# 22. Create variables of int, float, str, bool, list, tuple, set, and dict and display their types.
price = 20.9
print(f"{price} {type(price)}")
roll_number = 1
print(f"{roll_number} {type(roll_number)}")
name1 = 'ridhi'
print(f"{name1} {type(name1)}")
isgood = True
print(f"{isgood} {type(isgood)}")
menu1 =["pasta","pizza"," sweet corn"]
print(f"{menu1} {type(menu1)}")
menu2 = ("pav bhaji","momo","rajma chawal")
print(f"{menu2} {type(menu2)}")
menu3 ={
    "1" : "chole chawal",
    "2" : "biryani",
    "3" : "chole bhature"
}
print(f"{menu3} {type(menu3)}")
# 23. Swap two variables using a temporary variable.
num1 = 5
num2 = 6
print(num1,num2)
temp = num1
num1 = num2
num2 = temp
print(num1,num2)
# 24. Swap two variables without a temporary variable.
value1 = 6
value2 = 8
print(value1,value2)
value1 = value1+value2
value2 = value1-value2
value1 = value1-value2
print(value1,value2)
# 25. Convert a string containing a number to int.
value ="29"
convert = int(value)
print(value,type(value),convert,type(convert))

