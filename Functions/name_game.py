# define an input variable to prompt the user for a name
name = input('Enter your name:')
# print (name)

# create a function to create a truncated version of the name for using in the song
def trunc_name(name):
    if name == "a":
        return name.replace("a", "").lower()

print(trunc_name('Dan'))
