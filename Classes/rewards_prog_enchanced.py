class RewardsProgram:
    '''Customer information''' # be sure to include a docstring below the class name to describe the purpose of the class
    def __init__(self, cust_name, phone, email): # store customer name, customer phone, customer email
        self.cust_name = cust_name
        self.phone = phone
        self.email = email
        self.restaurants_visted=[]
        self.rewards_points = 0
         

    def profile(self): # first method and print the output for name, phone, and email
        print(f'''Name: {self.cust_name}
Phone: {self.phone}
Email: {self.email}''')


    def thank_you(self): # second method print out message
        print(f'Thank you {self.cust_name}, for visiting our restaurant!')
    
    
    def add_to_cust_list(self): # add the customer's name, phone, and email as a tuple to a list that is global in scope. 
        cust_list.append((self.cust_name, self.phone, self.email))

    def visit_rest(self):
        name_of_rest = input("Please enter name of the restaurant you are visiting: ")
        if name_of_rest not in self.restaurants_visted:
            cust_list.append(name_of_rest)
        total_bill = float(input("What was the total food bill for this visit?"))
        self.rewards_points += int(total_bill)
        print(f'''Points for this visit: {int(total_bill)}
Total rewards points earned: {self.rewards_points}
Thank you for visiting {name_of_rest}''')


        
cust_list = []

# create three instances of the class, making up sample data for three different customers. For each customer each methods.
cust_1 = RewardsProgram('jon deer', 7739689866, 'deer.jon@yahoo.com')
cust_2 = RewardsProgram('eric harris', 8157891233, 'eric.harris@gmail.com')
cust_3 = RewardsProgram('matt lee', 3128529633, 'matt.lee123@gmail.com')

# customer one
cust_1.profile()
cust_1.thank_you()
cust_1.add_to_cust_list()

# customer two
cust_2.profile()
cust_2.thank_you()
cust_2.add_to_cust_list()

# customer three
cust_3.profile()
cust_3.thank_you()
cust_3.add_to_cust_list()

# print the contents of cust-list to confirm that all customers have been added
print(cust_list)

# print output visit rest method for each customer
cust_1.visit_rest()
cust_2.visit_rest()
cust_3.visit_rest()
cust_3.visit_rest()
cust_3.visit_rest()