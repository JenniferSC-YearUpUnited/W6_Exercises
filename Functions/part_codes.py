# create a script that parses a part code
def part_code(supplier_code, product_num, size):
    '''Display information about a part code'''
    return f' {supplier_code}:{product_num}-{size}  Part# {product_num}, size {size}, supplied by {supplier_code}'
partcode1 = part_code('ABC', '123456', 'small')
partcode2 = part_code('DMJ', '345678', 'medium')
partcode3 = part_code('SUN', '1030', '16')
print(partcode1)
print(partcode2)
print(partcode3)

# sketch your ideas for the functions below
def get_supplier_code(supplier_code,):
    return f' {supplier_code}'
partcode4=part_code('ACME', '123', 'L')


def get_product_num(product_num):
    return f'{product_num}'
partcode5=part_code('DI', '12345', 'M')

def get_size(part_size):
    return f'{part_size}'
partcode6=part_code('ACE', '1', '12')

all_three = [partcode4, partcode5, partcode6]
# create variables to hold the three example part part codes
print(get_supplier_code({partcode4}))
print(get_product_num({partcode5}))
print(get_size({partcode6}))

# challenge
print(all_three)




    

