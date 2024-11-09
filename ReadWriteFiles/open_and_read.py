# f = open("about_me.txt", "r")
# print(f.read(50))
# print(f.read(50))
# print(f.readline(10))
# print(f.readline())
# print(f.readlines(1))
# print(f.readlines())
# print(f.readlines(1))
# print(f.readlines(10))
# print(f.readlines(10))
# print(f.readlines(100))
# print(f.readlines(-1))
# for i in range(1, 5):
#     print(f.readline())
# f.close()

with open("about_me.txt") as fifty:
    one = fifty.read(50)
  

with open("about_me.txt") as me:
    variables = me.readline()

one_list = []

for i in variables:
    one_list.append(i)

with open("about_me.txt") as hundred:
    hun = hundred.readlines(100)
   

print(f'''First 50 characters:{one}
Next four lines, as list by line: {one_list}
Next 100 characters, as list by line, rounded up to complete lines: {hun}''')




# changing the print statement to use read with 50 characters and adding a second print statement also using read with 50 characters changes my output by providing me with only a portion of my text file , cutting off in the middle.
# when I print using .readlines(1) I get my name as a string in a list on one line
# When I add another print statment with .readlines () with no argument and run them I get two list. The first list has a string with my name again and the second list has the rest of the text as a string.
# when I add anther print statement using .readlines(1) I get the same output, my first name as a string in a list and also get a second line of the text as a string, which was place of birth, in a list. 
# when I add another print statement using .readlines(10) I get my frist name as a string in a list, place of birth in a second line as a string in a list, and then I get a 3rd and 4th line of the text regarding the pet question and answer as a string in a list.
# when I add another print statement using .readlines(10) and comment out the first two print statements using. readlines(1) I get the same output as I did with the argument of 1. I get my name as a string in a list in the first line and on the second line I get place of birth as a string in a list.
# when I add another print statement using .readlines(100) I get the same output as I did when I printed out .readlines(10) the first time. My name as a string in a list for the first output, the second output has place of birth as a string in a list, then I have have the pet question and answer as a string in a list.
# when I add another print statement using .readlines(-1) I get the my first name as a string in a list, I get my place of birth as a string in a text, but this last output is one single list composed of the next two questions and answers together.