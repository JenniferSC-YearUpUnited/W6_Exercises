# valuerror exception
try:
    age = int(input("What is your age? "))
    # print(age)
except ValueError:
    print("Enter digits only / No letters!")
else:
    print(age)
finally:
    print("Please try again! ")    

# nameerror exception
try:
    age = ten
except NameError:
        print("Oh no age is not defined")
else:
        print(age)
finally: 
        print("Please quit")

# typeerror exception
try:
    name = input(" What is your name? ")
    age = int(input("How old are you? "))
    print(name + age)
except TypeError:
    print("Sorry, can't combine an intger with a variable please check your data type") 
else:
    print(name)
    print(age)
finally:
    print("Have a good day!")    

# syntaxerror
try:
    if 20 > 10
    print("Good job")
except SyntaxError:
    print("check your code")    
else: 
    print("You did it")    
finally:
    print("please try again")




