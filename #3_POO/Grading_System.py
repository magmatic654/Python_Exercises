import pkg
import pkg.utils

class Student:
    def __init__(self, name, grades = list()):
        self._name = name
        self._grades = grades

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name
    
    @property
    def grades(self):
        return self._grades
    
    @grades.setter
    def grades(self, new_grades):
        self.grades = new_grades

    def try_except(func):
        def wrapped(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError as error:
                return error
        return wrapped
    
    
    @try_except
    def add_grade(self, grade):
            if pkg.utils.is_number(grade) and pkg.utils.is_positive(grade):
                self.grades.append(grade)
                return 'Grado añadido correctamente'
            else: 
                raise ValueError('Solo se admiten números entre 0 y 100')
    
    @try_except
    def calculate_average(self):
        if len(self.grades) == 0: # Comprueba que hayan elementos en la lista de grados
            raise ValueError('No se cuenta con grados registrados')
        for grade in self.grades: 
            if not pkg.utils.is_number(grade): # Comprueba si el elemento de la lista es un valor numerico 
                raise ValueError(f'{grade} no es un valor númerico')
        return round(sum(self.grades) / len(self.grades), 2) # Retorna el promedio si pasa todas las prubas de error
    
    def is_passing(self):
        if self.calculate_average() >= 60:
            return True
        else:
            return False

# Ejecuta las pruebas
if __name__ == "__main__":
    pedro = Student('Pedro')
    # print(pedro.add_grade(100))
    print(pedro.add_grade(-100))
    # print(pedro.add_grade(10))
    print(pedro.grades)
    print(pedro.calculate_average())
    # print(pedro.grades)
    # pedro.add_grade(100)
    # print(pedro.grades)
    # print(pedro.calculate_average())