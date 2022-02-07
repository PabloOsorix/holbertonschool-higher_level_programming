#!/usr/bin/python3

"""File contains class square that inherits
from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class inherits from Rectanfgle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Method that defiines the instances of
        Square class"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Property size that modifies the width and
        height with the size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self) -> str:
        """instance that return the currently data
        of the object class Rectangle"""
        string = "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                               self.id, self.x,
                                               self.y, self.width)
        return string

    def update(self, *args, **kwargs):
        """Method that update atributtes of the Square
        and Rectangle classes"""
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
                if i > 4:
                    break
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    self.size = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value
                if key == 'id':
                    self.id = value

    def to_dictionary(self):
        """Module that returns the dictionary
        representation of Square class"""
        new_dict = {}
        for key, value in self.__dict__.items():
            if key == 'id':
                new_dict[key] = value
            else:
                new_dict[key[12:]] = value
        new_dict["size"] = new_dict["width"]
        del new_dict['width'], new_dict['height']
        return new_dict
