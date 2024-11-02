def conv_c_to_f(current_temp_C):
        fahrenheit = (current_temp_C * 9/5) + 32 
        return round(fahrenheit)
print(conv_c_to_f(100))
print(conv_c_to_f(45))
print(conv_c_to_f(19))
print(conv_c_to_f(0))
print(conv_c_to_f(-7))
print(conv_c_to_f(-40))

