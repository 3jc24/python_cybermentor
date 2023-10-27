#!/bin/python3
###########################
# Cyber Mentor full video
###########################
class Shoes:
    def __init__(self, name, price):
        self.name = name
        self.price = float(price)
    
    def budget_check (self, budget):
        if not isinstance (budget, (int, float)):
            print ("Invalid entry. Please enter a number.")
            exit()
    
    def change (self, budget):
        return (budget - self.price)

    def buy (self, budget):
        self.budget_check(budget)
        if budget >= self.price:
            print (f"You can cop {self.name}")
            if budget == self.price:
                print (f"You have exactly the money to buy {self.name}")
                exit ("Thanks for using the shoe buying app")
            else:
                print (f"you can buy {self.name} and you will have {self.change(budget)} left over (change)")
                exit ("Thanks for using this app")

            
