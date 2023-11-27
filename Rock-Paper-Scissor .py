# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 23:18:07 2023

@author: neill
"""

# A rock-paper-scissors game

# importing random package  
import random

# Using ASCII Arts for rock, paper, and scissors
# Adding the ASCII art into a variable

rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''

# Adding the game images into a list  
game_images = [rock, paper, scissors]

#Printing a welcome greeting
print("Welcome to the Rock-Paper-Scissor Game!")

while True:

# Taking input from the user's choice  
 user_choice = int(input(  
    "What do you wish to choose? Type 0 for Rock, 1 for Paper, 2 for scissor. \n => "))

 print("The User chooses: ")    

# print game image by user choice  
 print(game_images[user_choice])

# random computer choice  
 computer_choice = random.randint(0, 2)

 print("The Computer chooses: ")

# print game image by computer choice  
 print(game_images[computer_choice])

# rules in logic  
 if user_choice == 0 and computer_choice == 2:  
    print("Yayy! You win!! 😄")  
 elif computer_choice == 0 and user_choice == 2:  
    print("Oh oh.. You lose... 💀")  
 elif computer_choice > user_choice:  
    print("Oh oh.. You lose... 💀")  
 elif user_choice > computer_choice:  
    print("Yayy! You win!! 😄 ")  
 elif computer_choice == user_choice:  
    print("It's a draw 🤝.Oh that was a close one!")  
 elif user_choice >= 3 or user_choice < 0:  
    print("Oops! You typed an invalid number, You Lose.. 💀")  
 play_again = input("Play again? (y/n): ")
 if play_again.lower() != "y":
     break