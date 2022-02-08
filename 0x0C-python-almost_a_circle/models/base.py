#!/usr/bin/python3

"""Class that defines a base"""
import json
import os


class Base:
    """Class base of the other basses"""
    __nb_objects = 0

    def __init__(self, id=None):
        """instance that define the base
        of the class Base"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def reset_nb_instances():
        """resets the numeber of instances (created for testing)"""
        Base.__nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method that convert parameter list_dictionary
        to a json object."""
        string_json = []
        if list_dictionaries is None:
            return string_json
        string_json = json.dumps(list_dictionaries)
        return string_json

    @staticmethod
    def from_json_string(json_string):
        """Static method that return the list
        of the json string representation"""
        new_list = []
        if json_string:
            tmp = []
            new_list = json.loads(json_string)
            for i in range(len(new_list)):
                tmp.append(new_list[i])
            return tmp
        return new_list

    @classmethod
    def save_to_file(cls, list_objs):
        """Method that convert parameter list_object
        to json an save it content in a file.json"""
        if list_objs:
            my_list = []
            for i in range(len(list_objs)):
                my_list.append(cls.to_dictionary(list_objs[i]))
            with open("{}.json".format(cls.__name__),
                      mode="w", encoding="utf8") as file:
                file.write(cls.to_json_string(my_list))

    @classmethod
    def create(cls, **dictionary):
        """Class method that returns an instance
        with all attributes already set"""
        if cls.__name__ == "Rectangle":
            new_instance = cls(4, 4)
        else:
            new_instance = cls(4)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """Module that returns a list of instances"""
        my_list = []
        filename = str(cls.__name__)+".json"
        if os.path.exists(filename):
            with open(filename, encoding="utf-8") as my_file:
                dictionay = cls.from_json_string(my_file.read())
                for i in dictionay:
                    my_list.append(cls.create(**i))
        return(my_list)
