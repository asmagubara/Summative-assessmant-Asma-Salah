# -*- coding: utf-8 -*-
"""Willy's Wonka Vending Machine

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r9C7hoQjlBaLQ_ve-5LqWU94u1pYfgup
"""

import time
print ("Welcome to Willy's Wonka Vending Machine.")

# ask the user how much money they want to enter.
number_of_10p = int(input("How many 10 pence coins would you like to insert? "))
while number_of_10p < 0:
    number_of_10p = int(input("Please enter a positive number."))

number_of_20p = int(input("How many 20 pence coins would you like to insert? "))
while number_of_20p < 0:
    number_of_20p = int(input("Please enter a positive number."))

number_of_50p = int(input("How many 50 pence coins would you like to insert? "))
while number_of_50p < 0:
    number_of_50p = int(input("Please enter a positive number."))

number_of_100p = int(input("How many 1 pound coins would you like to insert? "))
while number_of_100p < 0:
    number_of_100p = int(input("Please enter a positive number."))

# making a variable to keep track of the total amount of money inserted into the vending machine.
change = round(((number_of_10p * 0.10) + (number_of_20p * 0.20) + (number_of_50p * 0.50) + (number_of_100p * 1.00)),2)

#informing the user of the total amount they have entered.
print ("\nIn total you have entered £", change)
time.sleep(2)

# defining variable for the prices of the five products. 
product_1, product_1_price = "Galaxy Chocolate", 0.95
product_2, product_2_price = "Pistachio Milkshake", 0.45
product_3, product_3_price = "Water", 0.55
product_4, product_4_price = "Milk Tea", 0.40
product_5, product_5_price = "Fanta", 0.81

# Creating variables to track the number of each items the cusotmer choose
galaxy_chocolate_bought = 0
pistachio_milkshake_bought = 0
water_bought = 0
milk_tea_bought = 0
fanta_bought = 0

# Informing the user of their choices available and the prices of each item they choose.
print ("There are 5 products available to pick from;\n")
time.sleep(2)
print ("Item: {}, Price {} ".format(product_1, product_1_price))
print ("Item: {}, Price {} ".format(product_2, product_2_price))
print ("Item: {}, Price {} ".format(product_3, product_3_price))
print ("Item: {}, Price {} ".format(product_4, product_4_price))
print ("Item: {}, Price {} ".format(product_5, product_5_price))
print ("")

# Ask the user to make a selection.
while change > 0:
    customer_choice = input("What would you like to buy? Type N when you are finished \n")
    if customer_choice == "Galaxy chocolate" or customer_choice == "galaxy chocolate" and change >= product_1_price:
        print ("You have chosen a", product_1, "these cost", product_1_price, "each,")
        change = round((change - product_1_price),2)
        galaxy_chocolate_bought = (galaxy_chocolate_bought + 1)
        print ("You have this much money remaining: £", change)

    elif customer_choice == "Pistachio Milkshake" or customer_choice == "pistachio milkshake" and change >= product_2_price:
        print ("You have chosen a", product_2, "these cost", product_2_price, "each,")
        change = round((change - product_2_price),2)
        pistachio_milkshake_bought = (pistachio_milkshake_bought + 1)
        print ("You have this much money remaining: £", change)

    elif customer_choice == "Water" or customer_choice == "water" and change >= product_3_price:
        print ("You have chosen a", product_3, "these cost", product_3_price, "each,")
        change = round((change - product_3_price),2)
        water_bought = (water_bought + 1)
        print ("You have this much money remaining: £", change)

    elif customer_choice == "Milk Tea" or customer_choice == "milk tea" and change >= product_4_price:
        print ("You have chosen a", product_4, "these cost", product_4_price, "each,")
        change = round((change - product_4_price),2)
        milk_tea_bought = (milk_tea_bought + 1)
        print ("You have this much money remaining: £", change)

    elif customer_choice == "Fanta" or customer_choice == "fanta" and change >= product_5_price:
        print ("You have chosen a", product_5, "these cost", product_5_price, "each,")
        change = round((change - product_5_price),2)
        fanta_bought = (fanta_bought + 1)
        print ("You have this much money remaining: £", change)

    elif customer_choice == "N" or customer_choice == "n":
        print ("\nHere is your transaction details:\n")
        print ("You purchased: ")
        print (product_1, "x", galaxy_chocolate_bought)
        print (product_2, "x", pistachio_milkshake_bought)
        print (product_3, "x", water_bought)
        print (product_4, "x", milk_tea_bought)
        print (product_5, "x", fanta_bought)
        print ("You have £", change, "remaining.")
        break

    elif change <= 0:
        print ("You have run out of money.")
        print ("\nHere is your transaction details:\n")
        print ("You purchased: ")
        print (product_1, "x", galaxy_chocolate_bought)
        print (product_2, "x", pistachio_milkshake_bought)
        print (product_3, "x", water_bought)
        print (product_4, "x", milk_tea_bought)
        print (product_5, "x", fanta_bought)
        break

    else:
        print ("There has been an error or you may not have enough credit.")