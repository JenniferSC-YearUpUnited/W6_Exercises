name = 'Jennifer Santos Custodio'
# Finding location of the substring I am looking for using the index
print(name.find('Jennifer'))
#print(full_name.rfind('Jennifer'))
print(name.find('Santos Custodio'))
#print(full_name.rfind('Santos Custodio'))

full_name = name[0:24]
first_name = name[0:8]
last_name = name[9:24]
print(full_name)
print(first_name)
print(last_name)
