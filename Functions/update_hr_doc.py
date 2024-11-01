# starting with a list extracted from an employee database, in the form of a list of tuples
hr_list=[
    ('0123','HR','Rebecca Yang','69000'), 
    ('0121','IT', 'Mark Blick', '67000'), 
    ('0068','IT','Kahna Larsen', '112000'),
    ('0234','OPS','Jim Smith','54000')]

# create variable for each tuple position 
employee1 = hr_list[0]
employee2 = hr_list[1]
employee3 = hr_list[2]
employee4 = hr_list[3]

#print(employee2)
# Updade Mark's last name to Blick-Hawley
# converting the tuple of position 1 into a list to change the items then inserting the updated name to the correct positon
# re- making the list into a tuple again.
change_employee2 = list(employee2)
#print(change_employee2)
change_employee2.remove('Mark Blick')
#print(change_employee2)
change_employee2.insert(2, 'Mark Blick-Hawley')
#print(change_employee2)
employee2 = tuple(change_employee2)
hr_list[1] = employee2
print(employee2)

# change Jim's department code from OPS to CS and update his salary to 60000
# converting the tuple into a list to change the items and inserting the updated info
change_employee4 = list(employee4)
#print(change_employee4)
change_employee4.remove('OPS')
#print(change_employee4)
change_employee4.remove('54000')
#print(change_employee4)
change_employee4.insert(1,'CS')
#print(change_employee4)
change_employee4.insert(3,'60000')
#print(change_employee4)
employee4 = tuple(change_employee4)
hr_list[3] = employee4
print(employee4)

# display the updated contents on multiple lines in the following format using th epipe symbol to separate each value 
# format the salry to us a comma
# convert to list again and print using the f'string format.
# cast the last position for the salary amount to an intenger to include the comma outside the index position but within the curly brackets 
change_employee2 = list(employee2)
change_employee4 = list(employee4)
print(f'{change_employee2[0]} | {change_employee2[1]} | {change_employee2[2]} | {int(change_employee2[3]):,}')
print(f'{change_employee4[0]} | {change_employee4[1]} | {change_employee4[2]} | {int(change_employee4[3]):,}')







