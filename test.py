import os
import numpy as np
import sys

def add(x, y):
    """"add"""
   return x + y

def ubtract(x, y):
    """"Subtract"""
   return x - y

def multiply(x, y):
    """"Multiply"""
   return x * y

def divide(x, y):
    """"Divide"""
   return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice(1/2/3/4):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))