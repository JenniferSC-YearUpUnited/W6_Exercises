name1 = input('Enter your name:').lower()


def trunc_name(name):        
    if name.startswith("a", 2,10):
        return name[2:]
    if name.startswith("a", 2,10):
        return name[2:]
    if name.startswith("e", 2,10):
        return name[2:]
    if name.startswith("i", 2,10):
        return name[2:]
    if name.startswith("o", 2,10):
        return name[2:]
    if name.startswith("u", 2,10):
        return name[2:]
    elif name.startswith("e", 0,1):
        return name
    elif name.startswith("i", 0,1):
        return name
    elif name.startswith("o", 0,1):
        return name
    elif name.startswith("u", 0,1):
        return name
    elif name.startswith("b", 0,1):
        return name[1:]
    elif name.startswith("c", 0,1):
        return name[1:]
    elif name.startswith("d", 0,1):
        return name[1:]
    elif name.startswith("f", 0,1):
        return name[1:]
    elif name.startswith("g", 0,1):
        return name[1:]
    elif name.startswith("h", 0,1):
        return name[1:]
    elif name.startswith("j", 0,1):
        return name[1:] 
    elif name.startswith("k", 0,1):
        return name[1:] 
    elif name.startswith("l", 0,1):
        return name[1:] 
    elif name.startswith("m", 0,1):
        return name[1:] 
    elif name.startswith("n", 0,1):
        return name[1:] 
    elif name.startswith("p", 0,1):
        return name[1:]
    elif name.startswith("q", 0,1):
        return name[1:]
    elif name.startswith("r", 0,1):
        return name[1:]
    elif name.startswith("s", 0,1):
        return name[1:]
    elif name.startswith("t", 0,1):
        return name[1:]
    elif name.startswith("v", 0,1):
        return name[1:]
    elif name.startswith("w", 0,1):
        return name[1:]
    elif name.startswith("x", 0,1):
        return name[1:]
    elif name.startswith("y", 0,1):
        return name[1:]
    elif name.startswith("z", 0,1):
        return name[1:]
    else:
        [print('ERROR! Can\'t be integers and must be 2 or more letters!')]





short_nam=trunc_name(name1)
def name_game():
    yield f'{name1}, {name1}, bo-b{short_nam}'
    yield f'banana fana fo-f{short_nam}'
    yield f'me my mo-m{short_nam}'
    yield f'{name1}!'

for x in name_game():
    print(x)


# when I enter integrs it does give me the output of error that I had created and none for the output when I print the output in the for loop of the name. 
# when I enter a single letter it does not give me the error but it also does not give me the output with just the letter and does not print it out anywhere in the name game after I enter it. 
# when I enter nothing and just hit enter at the prompt it does give me my error message I created and outputs None in the name game. 
# I was expecting for all the inputs to throw an error message and just not continue but they work although they produce a funny output that I do not want. 
# I would try to implement a try except block to check  for this type of issues. 
# I updated the error message for it to display can't be integers and must be 2 or more letters
# The example above is using pass because they do not want to give a response or raise an actual flag in the script to figure out what is wrong. Instead they just want to keep going or continue running the script.
# I think the logic is for them to see that if the name is an integer the output will not make any sense.
# I think the statement raise systemexit(0) means to break out of the loop if they would want to they have the option of just inputting a zero digit. I think this was used instead of break so if the user wants to keep trying inputting a valid name they can rather than just exiting the loop and quitting the program. 
