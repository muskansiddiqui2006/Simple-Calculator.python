# -*- coding: utf-8 -*-
"""class2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Wlhemy0m7sPp3qi819PbkEegTvAKVhd3

Class 2 Home Work
"""

num1 = float (input ("Enter first number:"))

operator = input("Enter operator(+,-,*,/):")

num2 = float (input("Enter second number:"))

if operator == '+':
  print("Result:", num1 + num2)

elif operator == '-':
    print("Result:", num1 - num2)

elif operator == '*':
     print("Result:", num1 * num2)

elif operator == '/':
     print("Result:", num1 / num2 if num2 !=0 else"Error! Divison by zero.")

else:
    print("Invalid operator")