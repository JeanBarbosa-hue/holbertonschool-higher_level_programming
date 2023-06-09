#!/usr/bin/python3

"""Class called BaseGeometry."""


class BaseGeometry:
    """Public instance that raises exception."""

    def area(self):
        """Exception of BaseGeometry."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value."""
        if isinstance(name, str):
            if type(value) is not int:
                raise TypeError(f"{name} must be an integer")
            if value <= 0:
                raise ValueError(f"{name} must be greater than 0")
