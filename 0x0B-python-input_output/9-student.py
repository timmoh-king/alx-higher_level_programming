#!/usr/bin/python3

"""class Student that defines a student by"""


class Student:
    def __init__(self, first_name, last_name, age):
        """declare public attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation"""
        return self.__dict__
