#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 2022

@author: Godday Okoduwa
         Ingrid Koumayeb
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class inherits from BaseModel

    Attribute:
        name (str): Public class attribute for Amenity's name
    """
    name = ''

    def __init__(self, *args, **kwargs):
        """
        init method for Amenity class

        Attributes:
            args (list): The list with arguments
            kwargs (dict): A dictionary with arguments
        """
        super().__init__(*args, **kwargs)
