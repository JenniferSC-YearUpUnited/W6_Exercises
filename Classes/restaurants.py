# got error message as restaurants did not take any arguements bc i didn't include to underscores for function init. Should be two underscores in front and before init. 
class Restaurants:
    '''varieties of restaurants'''  ## including a docstring below the class name to describe the purpose of the class
    def __init__(self, rest_name, food_type):  # should store two instance variables
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self): # add two methods to the class this is one and print an output
        print(f'{self.rest_name} serves {self.food_type}')

    def rest_open(self): # add two methods to the class this is two and print an output
        print(f'{self.rest_name} is open ')

# create three instances of the class for different types of restaurant 
bk= Restaurants('bubger king','burgers')
dd= Restaurants('donkin donnts','coffee')
tb= Restaurants('taco baco', 'tacos')

#call on each instance
dd.describe_rest()
dd.rest_open()

        


