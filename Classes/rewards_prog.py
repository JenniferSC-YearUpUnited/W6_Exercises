class RewardsProgram:
    '''Customer information''' # be sure to include a docstring below the class name to describe the purpose of the class
    def __init__(self, cust_name, phone, email): # store customer name, customer phone, customer email
        self.cust_name = cust_name
        self.phone = phone
        self.email = email
         

    def profile(self): # first method and print the output for name, phone, and email
        print(f'''Name: {self.cust_name}
Phone: {self.phone}
Email: {self.email}''')


    def thank_you(self): # second method print out message
        print(f'Thank you {self.cust_name}, for visiting our restaurant!')
    
    
    # def add_to_cust_list(self): # add the customer's name, phone, and email as a tuple to a list that is global in scope. 
        # global cust_list
        # cust_list = 

        
       

# create three instances of the class, making up sample data for three different customers. For each customer each methods.
cust_1 = RewardsProgram('jon deer', 7739689866, 'deer.jon@yahoo.com')
cust_2 = RewardsProgram('eric harris', 8157891233, 'eric.harris@gmail.com')
cust_3 = RewardsProgram('matt lee', 3128529633, 'matt.lee123@gmail.com')
cust_list = (f'''{cust_1.cust_name, cust_1.phone, cust_1.email}
{cust_2.cust_name, cust_2.phone, cust_2.email}
{cust_3.cust_name, cust_3.phone, cust_3.email}''')

# customer one
cust_1.profile()
cust_1.thank_you()
# cust_1.add_to_cust_list()

# customer two
cust_2.profile()
cust_2.thank_you()
# cust_2.add_to_cust_list()

# customer three
cust_3.profile()
cust_3.thank_you()
# cust_3.add_to_cust_list()

# print the contents of cust-list to confirm that all customers have been added
# print(cust_list)


