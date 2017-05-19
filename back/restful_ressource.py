import sys
import json
import make_json_serializable

class RestfulRessource():

    def __init__(self, schema):
        self.attributes = schema

    def update(self, attributes):
        for key in attributes:
            if key in self.attributes:
                self.attributes[key] = attributes[key]
        return self.attributes
    
    def get_attribute(self, key):
        if key in self.attributes:
            return self.attributes[key]
        else:
            return False

    def set_attribute(self, key, value):
        if key in self.attributes:
            self.attributes[key] = value

    def to_json(self):
        return self.attributes

    def __str__(self):
        return ",".join([str(self.attributes[key]) for key in self.attributes])