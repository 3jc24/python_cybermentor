#!/bin/python3
###########################
# Cyber Mentor full video
###########################

from Shoes import Shoes

low = Shoes ("And1", 30)
medium = Shoes ("Nike", 120)
hight = Shoes ("Adidas", 400)

try:
    shoe_budget = float(input ("Whats your shoe budget? "))
except ValueError:
    exit ("Please insert a number")

for shoes in (hight, medium, low):
    shoes.buy (shoe_budget)
