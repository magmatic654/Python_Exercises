def is_number(number):
    return True if type(number) == type(float()) or type(number) == type(int()) else False
        

def is_positive(number):
    return True if number >= 0 else False