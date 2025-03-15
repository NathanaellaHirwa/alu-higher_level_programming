#!/usr/bin/python3
import csv
import os

class Base:
    """Base class for other classes in the project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize a list of objects to a CSV file."""
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize objects from a CSV file."""
        filename = cls.__name__ + ".csv"
        objects = []
        if not os.path.exists(filename):
            return objects
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    obj = cls(int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[0]))
                elif cls.__name__ == "Square":
                    obj = cls(int(row[1]), int(row[2]), int(row[3]), int(row[0]))
                objects.append(obj)
        return objectsimport csv
import os

class Base:
    """Base class for other classes in the project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize a list of objects to a CSV file."""
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize objects from a CSV file."""
        filename = cls.__name__ + ".csv"
        objects = []
        if not os.path.exists(filename):
            return objects
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    obj = cls(int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[0]))
                elif cls.__name__ == "Square":
                    obj = cls(int(row[1]), int(row[2]), int(row[3]), int(row[0]))
                objects.append(obj)
        return objects
