# got error message as restaurants did not take any arguements bc i didn't include to underscores for function init. Should be two underscores in front and before init. 
class Restaurants:
    '''Summarize a restaurant'''  ## including a docstring below the class name to describe the purpose of the class
    def __init__(self, rest_name, food_type):  # should store two instance variables
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []

    def describe_rest(self): # add two methods to the class this is one and print an output
        print(f'{self.rest_name} serves {self.food_type}')

    def rest_open(self): # add two methods to the class this is two and print an output
        print(f'{self.rest_name} is open ')

    def add_num_served(self): # that accepts an input and adds the number served to the self number served attribute 
        num_served = int(input("How many customers served today? "))
        self.number_served += num_served
    
    def print_num_served(self): 
        print(f'{self.rest_name} has served {self.number_served} customers')

    def customer_rating(self): # method needs to accept an input of integers 1-5 and adds that number to the list of self customer ratings
        rating= int(input(f"How would you rate your experience today at {self.rest_name} on a scale of 1-5 (5 being excelent)? " ))
        self.customer_ratings.append(rating) 
        average_rate = sum(self.customer_ratings) / len(self.customer_ratings)   # calculate the average using the sume of the ratings list, divided by the list length
        if rating == float: # updating the method with conditional logic to account for different possible input types
            print("Invalid entry must be an integer. Please try again")
        elif rating <1:
            print("Invalid rating. Rate on a scale of 1-5 please")
        elif rating >5:
            print("Invalid rating. Rate on a scale of 1-5 please")
        else:
            print(f'Your rating was {rating}. The average rating for this restaurant is {average_rate}') 


# create three instances of the class for different types of restaurant 
bk= Restaurants('Bubger King','burgers')
dd= Restaurants('Donkin Donnts','coffee')
tb= Restaurants('Taco Baco', 'tacos')

#call on each instance
# dd.describe_rest()
# dd.rest_open()

# bk.describe_rest()
# bk.rest_open()

# tb.describe_rest()
# tb.rest_open()


# call on an instance for add number served and print number served methods
# bk.add_num_served()
# bk.add_num_served()
# bk.print_num_served()

# call an instance for customer rating method
# dd.customer_rating()
# dd.customer_rating()
# dd.customer_rating()
# dd.customer_rating()

# run for each of my example restaurants 
# bk.print_num_served()
# bk.add_num_served()
# bk.add_num_served()
# bk.add_num_served()
# bk.print_num_served()

# dd.print_num_served()
# dd.add_num_served()
# dd.add_num_served()
# dd.add_num_served()
# dd.print_num_served()

# tb.print_num_served()
# tb.add_num_served()
# tb.add_num_served()
# tb.add_num_served()
# tb.print_num_served()

# run for each of my example restaurants
bk.customer_rating()
bk.customer_rating()
bk.customer_rating()

dd.customer_rating()
dd.customer_rating()
dd.customer_rating()

tb.customer_rating()
tb.customer_rating()
tb.customer_rating()




