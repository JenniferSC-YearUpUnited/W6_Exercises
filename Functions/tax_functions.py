# create three functions
def get_soc_sec_tax(gross_pay):
    """returns the social security tax on the gross pay amount"""
    subtract = gross_pay * 0.062
    soc_sec_tax = gross_pay - subtract
    return f'${soc_sec_tax:.2f}'
print(get_soc_sec_tax(1200))

def get_medicare_tax(gross_pay):
    """returns the medicare tax on the gross pay amount"""
    subtract2 = gross_pay * 0.0145
    medicare_tax = gross_pay - subtract2
    return f'${medicare_tax:.2f}'
print(get_medicare_tax(1200))


def get_federal_tax(gross_pay,wh_code):
    """returns the federal tax withholding on the gross pay amount"""
    if wh_code == 0:
        subtract3 = gross_pay * 0.23
        federal_tax1 = gross_pay - subtract3
        return f'${federal_tax1:.2f}' 
    elif wh_code == 1:
        subtract4 = gross_pay * 0.21
        federal_tax2 = gross_pay - subtract4
        return f'${federal_tax2:.2f}' 
    elif wh_code == 2:
        subtract5 = gross_pay * 0.195
        federal_tax3 = gross_pay - subtract5
        return f'${federal_tax3:.2f}' 
    elif wh_code == 3:
        subtract6 = gross_pay * 0.185
        federal_tax4 = gross_pay - subtract6
        return f'${federal_tax4:.2f}' 
    elif wh_code >= 4:
        subtract7 = gross_pay * 0.1791
        federal_tax5 = gross_pay - subtract7
        return f'${federal_tax5:.2f}' 
    else:
        print('Error, try again!')
# call the function three times for each of the following examples        
print(get_federal_tax(750,0))        
print(get_federal_tax(1550,2))
print(get_federal_tax(1100,5))

