import pkg

class Rectangle:
    def __init__(self, length = 1, width = 1):
        self._length = length
        self._width = width
    
    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, new_length):
        self._length = new_length

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, new_width):
        self._width = new_width

    def try_catch(func):
        def wrapped(*args,**kwargs):
            try:
                return func(*args,**kwargs)
            except ValueError as error:
                return error
        return wrapped 
    
    def try_catch(func):
        def wrapped(*args,**kwargs):
            try:
                return func(*args,**kwargs)
            except ValueError as error:
                return error
        return wrapped 

    def calculateArea(self):
        return self._length * self._width
    
    def calculatePerimeter(self):
        return self._length * 2 + self.width * 2
    
    @try_catch
    def resize(self, new_length, new_width):
        if new_length < 0 or new_width < 0: 
            raise ValueError('No se pueden introducir valores negativos o 0')
        self.length = new_length
        self.width = new_width
    
if __name__ == '__main__':
    rectangle = Rectangle(10, 5)
    print(rectangle.calculateArea())
    print(rectangle.calculatePerimeter())

    rectangle2 = Rectangle()
    print(rectangle2.calculateArea())
    print(rectangle2.calculatePerimeter())
    
    rectangle3 = Rectangle(5, 9)
    print(rectangle3.calculateArea())
    print(rectangle3.calculatePerimeter())
    rectangle3.resize(10, 20)
    print(rectangle3.calculateArea())
    print(rectangle3.calculatePerimeter())
    print(rectangle3.resize(10, -20))
    print(rectangle3.resize(-10, 20))
    print(rectangle3.resize(-10, -20))
    print(rectangle3.calculateArea())
    print(rectangle3.calculatePerimeter())
