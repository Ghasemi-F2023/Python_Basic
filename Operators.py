'''
Exercise 01
Operators
Get a number as circle diameter, and calculate the circle area
'''
import math 
circumference=float(input('input:'))
Radius=circumference/2
area = (Radius*Radius)* math.pi
area_rond=round(area,3)
print('output (print): Circle area is {}'.format(area_rond))
---------------------------------------------------------------
'''
Exercise 02
Operators
Get width, height and length ,then calculate and print the surface area and volume of a cuboid
'''
width=int(input('input1: '))
height =int(input('input2: '))
length =int(input('input3: '))
Volume=float(width*height*length)

multiplication_width_height=(width*height)*2
multiplication_width_length=(width*length)*2
multiplication_height_length=(height*length)*2

Surface=float(multiplication_width_height+multiplication_width_length+multiplication_height_length)
print('input1:{0}, input{1}, input{2}, output (print): Volume of cuboid is {3} and Surface area\
of cuboid is {4}'.format(width,height,length,Volume,Surface))
-----------------------------------------------------------------
'''
Exercise 03
Operators
input(2 number) and print sum, division, subtraction, multiplication
'''
Number1=int(input('input_1:'))
Number2=int(input('input_2:'))

sum=Number1+Number2
division=Number1/Number2
subtraction=Number1-Number2
multiplication=Number1*Number2

print('input_1: {0}, input_2: {1}, output:sum={2},  divistion={3}, subtraction={4}, multiplication={5}'\
      .format(Number1,Number2,sum,division,subtraction,multiplication))
-----------------------------------------------------------------------
'''
Exercise 04
Operators
Get two string, concatenate them and print the result!
'''
str1=input('input_1:')
str2=input('input_2:')
output=str1+' '+ str2
print('input_1:{0}, input_2:{1}, output: result is "{2}"'.format(str1,str2,output))
--------------------------------------------------------------------------
'''
Exercise 05
Operators
Write a Python program to convert Fahrenheit to Celcius.
'''
fahrenheit = float(input("Enter temperature in fahrenheit: "))
celsius = (fahrenheit - 32)/1.8
print('input:{0} , output:{1} degree Fahrenheit is equal to {2} degree Celuius' .format(fahrenheit,fahrenheit,celsius))
---------------------------------------------------------------------------
'''
Exercise 06
write a code to create following pattern
'''
for i in range(7):
  for j in range(i):
     print('#', end='')
  print('')