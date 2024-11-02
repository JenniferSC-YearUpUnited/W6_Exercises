# define function with five parameters and format to display the data as you would on an adddress label
def display_mailing_label(name, address, city, state, zip):
    return f'''{name}
{address}
{city}, {state} {zip}'''

print(display_mailing_label(name='George Boss', address='3910 S Damen Ave', city='Chicago', state='IL', zip='60501'))

# define functin with one parameter defined to accept any number of arguments, each argument being an integer. Add the given arguments together and display the result as [number+number2+number3]=result
def add_number(*integers):
    sum = 0
    for x in integers:
        sum += x
    return f'{integers} = {sum}'

print(add_number(2,2,2))
 
# second function should accept two parameters. Compute and display the change due in the following format:
def display_receipt(total_due, amount_paid):
    for x in total_due, amount_paid:
        difference = abs(amount_paid - total_due)
    if amount_paid < total_due:
        return f'Bill not paid in full! Remaining balance is ${difference:.2f}'
    for i in total_due, amount_paid:
        change = abs(total_due - amount_paid)
        return f'''
Total Due: ${total_due:.2f}
Amount Paid:${amount_paid:.2f}
        
Change Due:${change:.2f}'''
    
    
print( display_receipt(89.50,100))    

# call display_ mailing_label at least twice with data for two different people
print(display_mailing_label('Ana Williams','3340 W John Blvd','Evanston','IL','54677'))
print(display_mailing_label('Bob Jenkins','9910 N Pope Ave','Elgin', 'IL','99101'))

# call add _numbers three times with one number,two numbers, and your choice of however many numbers
print(add_number(5))
print(add_number(4,4))
print(add_number(9,9,9,9))

# call display_receipt() three times. The first time, overpay the bill. The second time, pay
print(display_receipt(110.59,200))
print(display_receipt(67.75,67.75))
print(display_receipt(90.10,50.50))

