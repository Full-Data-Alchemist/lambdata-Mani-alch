"""
OOP examples for module 2
"""

import pandas as pd
import numpy as np




class MyDataFrame(pd.DataFrame):
    """
    inherinting from pandas data frame class to extent on it for personal tool creation
    """
    def num_cell(self):
        cell_count = self.shape[0] * self.shape[1]
        return cell_count

class BareMinClass:
    """
    Bare Minimum Class
    """
    #TODO
    pass
# note to self this stuff get's meta
class complex():
    """
    #TODO
    """
    def __init__(self, realpart, imagpart):
        """
        constructor for complex numbers
        complex numbers have real and imaginary parts.
        """
        self.r = realpart
        self.i = imagpart 
    def add(self, other_complex):
        """
        adder 
        """
        self.r += other_complex.r
        self.i += other_complex.i

    def  __repr__(self):
        return '({}, {})'.format(self.r, self.i)


class SOcialMediaUser:
    """
    #TODO
    """
    def __init__(self, location, upvotes=0):
        self.name = str(name)
        self.location = location
        self.upvotes = int(upvotes)

    def recieve_upvotes(self, num_upvotes):
        """
        #function updates the upvote count
        """
        self.upvotes += num_upvotes


    def is_popular(self):
        """
        #function returns if a user is popular
        """
        return self.upvotes > 100
    

class Animal:
    """
    general representation of animals
    """
    def __init__(self, name, weight, diet_type):
        self.name = str(name)
        self.weight = float(weight)
        self.diet_type = diet_type

    def run(self):
        return f'Vroom Vroom go qick!!!'

    def eat(self, food):
        return f'Huge fan of that {str(food)}'

class Sloth(Animal):
    """

    """
    def __iinit__(self, name, weight, diet_type, num_naps):
        super().__init__(name, weight, diet_type)
        self.num__naps = num_naps
    
    def say_something(self):
        """
        what does the sloth say
        """
        return f'this is a sloth of typIng'

    def run(self):
        """
        what is the sloth speed
        """
        return f'I am a slow guy'







if __name__ == "__main__":
    num1 = complex(3, 5)
    num2 = complex(4, 2)
    num1.add(num2)
    print(f"{num1.r}{num1.i}")

    user1 = SOcialMediaUser('Mani', 'the west', 10000)
    user2 = SOcialMediaUser('Nick', 'the North', 755)
    user3 = SOcialMediaUser('Kai', 'the South', 100)
    user4 = SOcialMediaUser(name='Pikkon', location='the East', upcotes=1)
    print(f'{user4.name} is popular: {user4.is_popular(), user4.upvotes}')
    print(f'{user3.name} is popular: {user3.is_popular(), user3.upvotes}')
