"""
Source: https://py.checkio.org/en/mission/3-chefs/

Description:
You are the owner of a cafe where 3 chefs work: a JapaneseCook, RussianCook and ItalianCook. Each of them can prepare the national food and beverage:
- JapaneseCook: Sushi and Tea;
- RussianCook: Dumplings and Compote;
- ItalianCook: Pizza and Juice.
Your task is to create 3 different subclasses (one for each chef) which are the children of an AbstractCook and have these methods:
- add_food(food_amount, food_price), which add to the client's order the value of the food which he had chosen;
- add_drink(drink_amount, drink_price), which add to the client's order the value of the drink which he had chosen;
- total(), which returns a string like: 'Foods: 150, Drinks: 50, Total: 200', and for the each chef instead of the Foods and Drinks will be the national food and drink that he’s used.
Every client can choose only one chef. 
"""

class AbstractCook:
    f_total = 0
    d_total = 0
    def add_food(self, food, f_amount):
        self.f_total += food * f_amount
        return self.f_total  
    def add_drink (self, drink, d_amount):
        self.d_total += drink * d_amount
        return self.d_total
        
    def total(self):
        t = self.f_total + self.d_total
        return "{}: {}, {}: {}, Total: {}".format(self.food_name, self.f_total, self.drink_name, self.d_total, t)
        
class JapaneseCook(AbstractCook):
    food_name, drink_name = ("Sushi", "Tea")

class RussianCook(AbstractCook):
    food_name, drink_name = ("Dumplings", "Compote")

class ItalianCook(AbstractCook):
    food_name, drink_name = ("Pizza", "Juice")
    
