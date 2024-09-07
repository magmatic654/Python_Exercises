def check_negative(number):
    if number < 0:
        raise ValueError('No se admiten números negativos')

def check_zero(number):
    if number == 0:
        raise ValueError('No se admite 0')

def check_negative_and_zero(number):
    check_negative(number)
    check_zero(number)
    return True

if __name__ == '__main__':
    pass