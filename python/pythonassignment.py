# practice :

print("hello world")
print("i am tisha")
print("i am using python file")

# practice

num1 = int(input("enter your value :"))
num2 = int(input("enter your sec value :"))
total = num1 + num2
print("total :",total)

# Exercise 1: Mailing Address (Solved, 9 Lines) 
# Createaprogramthatdisplaysyournameandcompletemailingaddress.
# Theaddress should be printed in the format that is normally used in
# the area where you live. Your program does not need to read any input from the user.


print("my name is tisha")
print("i live in karachi and my address is a.b.c street")


# Exercise 2: Hello (9 Lines) Write a program that asks the 
# user to enter his or her name. The program should respond
#  with a message that says hello to the user, using his or her name.

user_name = str(input("WHAT IS YOUR NAME :"))
print("hello",user_name)

# Exercise 3: Area ofaRoom (Solved, 13 Lines) Write a program that asks the user to enter the width and length of a room.
#  Once these values have been read, your program should compute and display the area of the room.
#  Thelengthandthewidthwillbeenteredasfloating-pointnumbers.
# Include units in your prompt and output message; either feet or meters, depending on which unit you are more comfortable working with.

length = float(input("write the length value :"))
width = float(input("write the width value :"))
Area = length * width
print("this is the room square feet", Area)

# Exercise 4: Area ofaField (Solved, 15 Lines) Create a program that reads the length and width 
# of a farmer’s field from the user in feet. Display the area of the field in acres. Hint: There are 43,560 square feet in an acre.

length =float(input("write the feet of length :"))
width =float(input("write the feet of width :"))
Area = length * width / 43560
print("this is the area acres of suare feet" , Area)

# Exercise 7: SumoftheFirstn PositiveIntegers (Solved, 11 Lines) Write a program that reads a positive integer,
#  n, from the user and then displays the sum of all 
# of the integers from 1 to n. The sum of the first n positive integers can be computed using the formula: sum = (n)(n +1) 2

n = int(input("enter the sum value : "))
sum =  n *( n + 1) / 2
print("this is your sum value after calculation",sum)

# Exercise 8: WidgetsandGizmos (15 Lines) An online retailer sells two products: widgets
#  and gizmos. Each widget weighs 75 grams. Each gizmo weighs 112 grams. Write a program that
#  reads the number of widgetsandthenumberofgizmos
#  fromtheuser.Thenyourprogramshouldcompute and display the total weight of the parts.

widget = int(input("enter the widget value"))
gizmo = int(input("enter the gizmo value"))
widget_value = 75
gizmo_value =  112 
value1 = widget * widget_value
value2 = gizmo * gizmo_value
sum = value1 + value2
print("this is the answer",sum)

# Exercise 10: Arithmetic (Solved, 22 Lines) Createaprogram
# thatreadstwointegers,a andb,fromtheuser.Yourprogramshould compute and 
# display: • The sum of a and b • The difference when b is subtracted from a • The product
#  of a and b • The quotient when a is divided by b • The 
#  remainder when a is divided by b • The result of log10 a • The result of ab

variable_a = int(input("Enter the value of first variable :"))
variable_b = int(input("Enter the value of second variable :"))
sum = variable_a + variable_b
print ("this is the answer" ,sum)

variable_a = int(input("Enter the value of first variable :"))
variable_b = int(input("Enter the value of second variable :"))
sub= variable_a - variable_b
print ("this is the answer" ,sub)

variable_a = int(input("Enter the value of first variable :"))
variable_b = int(input("Enter the value of second variable :"))
mul= variable_a * variable_b
print ("this is the answer" ,mul)

variable_a = int(input("Enter the value of first variable :"))
variable_b = int(input("Enter the value of second variable :"))
div= variable_a / variable_b
print ("this is the answer" ,div)

variable_a = int(input("Enter the value of first variable :"))
variable_b = int(input("Enter the value of second variable :"))
exp= variable_a ** variable_b
print ("this is the answer" ,exp)

variable_a = int(input("Enter the value of first variable :"))
variable_b = int(input("Enter the value of second variable :"))
mol= variable_a % variable_b
print ("this is the answer" ,mol)
