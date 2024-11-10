pi = open("C:\\Users\\Student\\YUU-LearnToCode\\DataAnalytics\\week_6\\W6_Exercises\\ReadWriteFiles\\pi_million_digits.txt", "r")
# print(pi.readline())

user_birthday = input("Enter your birthday in the format MMDDYY: ")
pi_lines = pi.readlines()
birthday_found = None
for i in pi_lines:
    if user_birthday in i:
        print("Your birthday is in the first million digits of pi")
        birthday_found = 1
        break
    else:
        continue

pi_string = ''
for i in pi_lines:
    pi_string += i.strip()

if birthday_found != 1:
        print("Sorry your birthday was not found in the first million digits of pi")
else: 
    birthday_position = pi_string.index(user_birthday)-1
    print(f'Your birthday begins at a decimal place {birthday_position}')



# The -1 at the end is consider to start the decimal position of your birthday after the 3 which has a zero positon of one and then after the decimal place which has a position of 1. Posiiton 2 is after the decimal place so that would give us the right position to find the decimal posiiton of a certain birthday.


# print(pi_lines[0:2])
# print(len(pi_lines[0]))
pi.close()



