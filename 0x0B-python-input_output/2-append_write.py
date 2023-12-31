#!/usr/bin/python3
"""A function that appends a string at the end of a text file (UTF8)."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
