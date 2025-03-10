#!/usr/bin/python3
"""
Module to read and print the contents of a file to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The path to the file to read.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")

