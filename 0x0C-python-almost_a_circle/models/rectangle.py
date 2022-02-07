#!/usr/bin/python3

"""Class that defines a Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Class inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Method that defines the instances of the
        rectangle class."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Property that return the width instance modify
        by the setter"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Property that retuns the height instace modify
        by the setter"""
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Property that returns the x instance modify
        by the setter"""
        return self.__x

    @x.setter
    def x(self, value):
        if isinstance(value, int) is False:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """property that returns the y instasnce modify
        by the setter"""
        return self.__y

    @y.setter
    def y(self, value):
        if isinstance(value, int) is False:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Instance that defines the area of
        recatangle object, using width and height atributte"""
        return self.__width * self.__height

    def display(self):
        """public method that print the Rectangle
        instance with the character (#)"""
        for i in range(self.y):
            print()
        for j in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self) -> str:
        """instance that return the currently data
        of the object class Rectangle"""
        string = "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                  self.id, self.__x,
                                                  self.__y, self.__width,
                                                  self.__height)
        return string

    def update(self, *args, **kwargs):
        """This public method assigns an
        argument to each attribute updating
        object of Rectangle class by args or kwargs:"""
        if args:
            for i in range(len(args)):
                if i == 0:
                    super().__init__(args[i])
                if i == 1:
                    self.__width = args[i]
                if i == 2:
                    self.__height = args[i]
                if i == 3:
                    self.__x = args[i]
                if i == 4:
                    self.__y = args[i]
                if i > 4:
                    break
        else:
            if kwargs:
                for key, value in kwargs.items():
                    if key == 'id':
                        super().__init__(value)
                    if key == 'width':
                        self.__width = value
                    if key == 'height':
                        self.__height = value
                    if key == 'x':
                        self.__x = value
                    if key == 'y':
                        self.__y = value

    def to_dictionary(self):
        """Method that return returns the
        dictionary representation of a
        Rectangle:"""
        new_dict = {}
        for key, value in self.__dict__.items():
            if key == "id":
                new_dict[key] = value
            else:
                new_dict[key[12:]] = value
        return new_dict
