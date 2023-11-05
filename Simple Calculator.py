# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 10:59:04 2023

@author: neill
"""

def calc(n1,n2,operator):
    if operator == '+':
        result = n1+n2
    elif operator == '-':
        result = n1-n2
    elif operator == '*':
        result =  n1*n2
    elif operator == '/':
        result = n1/n2
    elif operator == '^':
        result =  n1**n2
    elif operator == '%':
        result = n1%n2
    else:
        raise ValueError('Invalid operator entered. Please enter a valid one.')
    
    if result.is_integer():
        result = int(result)
        
    return result

cont_calculating = True
while cont_calculating is True:
    number1 = float(input('Enter the first value: '))
    op = input('Enter operator from the following (+,-,*,/,^,%): ')
    number2 = float(input('Enter the second value: '))
    print(number1,op,number2)
    result=calc(number1,number2,op)
    print('=',result)
    Yes_Or_No = input('Continue? (y/n): ')
    if Yes_Or_No == 'n':
        cont_calculating = False