def check_Zero(num):
    if num == 0:
        raise ValueError('No se acepta el número 0')

def check_Negative(num):
    if num < 0:
        raise ValueError('No se aceptan números negativos')

def check_Zero_and_Negative(num):
    check_Negative(num)
    check_Zero(num)

