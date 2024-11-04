# define an input variable to prompt the user for a name
# create a function to create a truncated version of the name for using in the song
def trunc_name(name):
    name = input('Enter your name:').lower()
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
        [print('ERROR!')]

## NEED HELP: getting the last two consonants to drop
# print(trunc_name("STAN"))



# define another function called name_game(). This wil be a generator function.
# create a separate yield statement for each line of the game 
# using a for loop print the output of the name_game() function for carly, CHARLIE, Aidan, Braden, Billy Bob
def name_game():
    yield "What is your name?"
    name = input('Enter your name:').lower()
    yield f'{name[0:10]}, {name[0:10]}, bo-b{name[1:10]}'
    yield f'banana fana fo-f{name[1:10]}'
    yield f'me my mo-m{name[1:10]}'
    yield f'{name}!'

for x in name_game():
    print(x)

# ran into unexpected outputs- need to correct my code logic as I need to incorporate my truncate function 





