# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 10:05:48 2023

@author: neill
"""

import random
import string

def generate_password(length, complexity):
    if complexity == "low":
        characters = string.ascii_letters + string.digits
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "high":
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_letters.upper() + string.punctuation.replace('!','')
    else:
        print("Invalid complexity level. Please choose 'low', 'medium', or 'high'.")
        return

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Hello and welcome to the Password Generator!")
    length = int(input("Please enter the desired length of the password: "))
    complexity = input("Please, enter the desired complexity level (low, medium, high): ")

    password = generate_password(length, complexity)

    if password:
        print("Here is your successfully generated password: {password}")

if __name__ == "__main__":
    main()