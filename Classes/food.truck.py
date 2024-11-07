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

class FoodTruck(Restaurants): # bottom of the script define a new child class and inclue docstring
    '''FoodTruck bookings'''
    def __init__(self, rest_name, food_type):
        super().__init__(rest_name, food_type) # taking in the info from the parent class
        self.private_bookings = 'N' # one of two new attributes
        self.truck_location = ""  # two of two new attributes

    def accepts_private_bookings(self): # new method that prompts input for booking and updates the value of self private bookings. 
        acceptance = input("Does this food truck accept private bookings? Y/N ")
        self.private_bookings = acceptance
        if acceptance is "Y":
            take = "takes"
        elif acceptance is "N":
            take = "does NOT take"
        else:    
             print('Invalid answer. Please type Y for yes or N for no')
        print(f'This food truck currently {take} private bookings')  # adding an if elif else statement for yes it does take bookings or not

    def relocate_truck(self):  # new method that prompts user to enter truck's current address
        loc = input("Please enter truck's current location(street address + city) ")
        self.truck_location = loc
        print(f'Truck is currently located at {loc}')         

# create an instance of the class for a food truck
bk = FoodTruck('Bubger King','burgers') 


#call on the child instance
bk.accepts_private_bookings()
bk.relocate_truck()







