 class Restaurants:
    '''Summarize a restaurant'''  ## including a docstring below the class name to describe the purpose of the class
    def __init__(self, rest_name, food_type):  # should store two instance variables
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self): # add two methods to the class this is one and print an output
        print(f'{self.rest_name} serves {self.food_type}')

    def rest_open(self): # add two methods to the class this is two and print an output
        print(f'{self.rest_name} is open ')

# create three instances of the class for different types of restaurant 
bk= Restaurants('Bubger King','burgers')
dd= Restaurants('Donkin Donnts','coffee')
tb= Restaurants('Taco Baco', 'tacos')

#call on each instance
dd.describe_rest()
dd.rest_open()

bk.describe_rest()
bk.rest_open()

tb.describe_rest()
tb.rest_open()


        


