def conv_f_to_c(current_temp_F):
        celsius = (current_temp_F - 32) * 5 / 9 
        return f'''
current_temp_F = {current_temp_F}
current_temp_C= {round(celsius)}'''
print(conv_f_to_c(212))
print(conv_f_to_c(90))
print(conv_f_to_c(72))
print(conv_f_to_c(32))
print(conv_f_to_c(0))
print(conv_f_to_c(-40))
