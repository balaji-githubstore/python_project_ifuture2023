""" Module contains area related formulae by balaji"""
import math

author_name = "bala"


def area_of_cirlce(radius):
    result = math.pi * radius * radius
    return result


# method for calculating area of triangle
def area_of_triangle(base, height):
    return (base * height) / 2


# method for calculating area of square


# method for calculating area of Trapezoid
def area_of_trapezoid(base1, base2, height):
    return (base1 + base2) * height / 2


def print_module_description():
    print("Contains Area related formalae!!")
