# create a variable named doubler that uses a lambda function to double whatever argument it receives
doubler = lambda n: n * 2
print(doubler(8))
print(doubler(-4))
print(doubler('banana'))

# create a tripler variable using similar logic but multiplying the supplied argument by 3(instead of 2) and test it out with the same sample values
tripler = lambda n: n * 3
print(tripler(8))
print(tripler(-4))
print(tripler('banana'))

# if you want to create a similar multiplier variable for numbers 4 through 10, how can you save yourself some code by putting this lambda within a function? Create a function and use it to create the muliplier variables
def multiplier(multiplier):
    return lambda n: n *(multiplier)

quadrupler = lambda n: n * 4
quintupler = lambda n: n * 5
sextupler = lambda n: n * 6
septupler = lambda n: n * 7
octupler = lambda n: n * 8
nonupler = lambda n: n * 9
decupler = lambda n: n * 10
# print each of the new variables once with a sample value as the argument
print (f'Multiply by 4 equals: {quadrupler(3)}')
print(f'Multiply by 5 equals: {quintupler(4)}')
print(f'Multiply by 6 equals: {sextupler(5)}')
print(f'Multiply by 7 equals: {septupler(6)}')
print(f'Multiply by 8 equals: {octupler(7)}')
print(f'Multiply by 9 equals: {nonupler(8)}')
print(f'Multiply by 10 equals: {decupler(9)}')

