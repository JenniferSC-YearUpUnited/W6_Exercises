class Restaurant:
    '''varieties of restaurants'''
    
    def _init_(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self):
        print(f'{self.rest_name} serves {self.food_type}')

    def rest_open(self):
        print(f'{self.rest_name} is open ')        

bubger_kirg = Restaurant('whoopers','burgers')
donkin_donnts = Restaurant('hot coffe','coffee')
tacobaco = Restaurant('soft taco', 'tacos')

print(f'The resturant I like is {bubger_kirg.rest_name}')
print(f'{bubger_kirg.rest_name} is {bubger_kirg.food_type}')
bubger_kirg.rest_open()


        


