import datetime
# define variable called today that represents the current dte and time
today= datetime.datetime.now()
#print(today)
# identify the day of the week, month day, year
print(today.strftime(f'Today is {"%A"}, {"%B"} {"%d"}, {"%Y"}'))

# define a variable for your birthday 
bday = datetime.date(1994,9,19) # adding my birthdate inside the parentheses
#print(bday)
print(bday.strftime(f'My birthday is {"%m"}/{"%d"}/{"%Y"}'))

# define a variable for ninety_d which will be used to represent the date 90 days from today.
ninety_d = today + datetime.timedelta(days=90)
print(ninety_d.strftime(f'90 days from today is {"%B"} {"%d"}, {"%Y"}'))

# define a variable for dinner_time 
dinner_time = datetime.time(12,30,) # adding the time for the next day as I do not want it to display AM. I want to display PM
print(dinner_time.strftime(f"Let's meet for dinner at {"%I"}:{"%M"}:{"%p"}"))