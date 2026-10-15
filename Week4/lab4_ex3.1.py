# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 09:29:11 2022

@author: minut
"""

def add(num1,num2):
    n = num1 + num2
    return n

def subtract (num1,num2):
    n = num1 - num2
    return n

def multiply(num1,num2):
    n = num1 * num2
    return n    

def divide (num1,num2):
    if num2 == 0:
        return "Error: Division by zero"
    n = num1 / num2
    return n

def calculator(num1,num2,operator):
    if operator == "+":
        return add(num1,num2)
    elif operator == "-":
        return subtract(num1,num2)
    elif operator == "*":
        return multiply(num1,num2)
    elif operator == "/":
        return divide(num1,num2)
    else:
        return "Invalid operator. Please use +, -, *, or /."

def read_number():
    n1= int(input("Enter a interger : "))
    n2 = int(input("Enter a interger : "))
    o = input("Enter a operator : ")
    return n1, n2, o

def main():
    n = read_number()
    result = calculator(n[0], n[1], n[2])
    print("Result of %d %s %d is %s" %(n[0], n[2], n[1], result))

if __name__ == "__main__":
    main()