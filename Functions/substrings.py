full_name = 'Eric Harris'
#Finding location of the space I am looking for using the index
print(f'The space in the name is position {full_name.find(" ")}')

#using f string
print(f'Full name:{full_name}')
print(f'First name:{full_name[0:4]}')
print(f'Last Name: {full_name[5:11]}')



# def name_finder(full_name, first_name, last_name):
#     return f'''Full Name:{full_name}
# First Name:{first_name}
# Last Name:{last_name}'''
# print(name_finder('Bob Lee', 'Bob', 'Lee'))
# print(name_finder('John Doe', 'John', 'Doe'))
# print(name_finder('Grace Flores', 'Grace', 'Flores'))
# print(name_finder('JB Oinonen', 'JB', 'Oinonen'))

# added the print statement in return but it gave me an error message so I did the f string without the print function. 
#     print(f'Full Name: {Full_Name}')
#     print(f'First Name: {First_Name}')
#     print(f'Last Name: {Last_Name}')
#work on the return statement - do not want to get none.

#challenge:
def name_finder(**kwargs):
    return kwargs
person1 = name_finder(one_word ='Lorde') 
person2 = name_finder(two_words ='Billie Eilish')
person3 = name_finder(three_words ='Megan Thee Stallion')
print(person1)
print(person2)
print(person3)
