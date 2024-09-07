#!/usr/bin/python3
import pydoc
import sys
import os

# Caesar encoding, for use with decoding below
ENCODING = {
    'y': 'a',
    'h': 'b',
    'v': 'c',
    'x': 'd',
    'k': 'e',
    'p': 'f',
    'z': 'g',
    's': 'h',
    'a': 'i',
    'b': 'j',
    'e': 'k',
    'w': 'l',
    'u': 'm',
    'q': 'n',
    'n': 'o',
    'l': 'p',
    'm': 'q',
    'f': 'r',
    'o': 's',
    'i': 't',
    'g': 'u',
    'j': 'v',
    't': 'w',
    'd': 'x',
    'r': 'y',
    'c': 'z',
    '3': '0',
    '8': '1',
    '4': '2',
    '0': '3',
    '2': '4',
    '7': '5',
    '5': '6',
    '9': '7',
    '1': '8',
    '6': '9'
 }

"""An ingredient has an amount and a description.
For example: an Ingredient could have "1 cup" as the amount and "butter" as the description."""
class Ingredient():
    def __init__(self, amount, description) -> None:
        self.amount = amount
        self.description = description


def decode_string(str):
    """Given a string named str, use the Caesar encoding above to return the decoded string."""
    decoded_string = ''
    for character in str:
        if character in ENCODING:
            decoded_string += ENCODING.get(character)
        else:
            decoded_string += character
    return decoded_string


def decode_ingredient(line):
    """Given an ingredient, decode the amount and description, and return a new Ingredient"""
    if '#' not in line:
        raise Exception('Unable to parse Ingredient missing # in line')
    decoded_amount, decoded_ingredient = decode_string(line).split('#', 1)
    return Ingredient(decoded_amount, decoded_ingredient)


def main():
    """A program that decodes a secret recipe"""
    secret_recipe_file = open("secret_recipe.txt", "r")
    decoded_recipe_file = open("decoded_recipe.txt", "w")

    while secret_line := secret_recipe_file.readline():
        ingredient = decode_ingredient(secret_line)
        decoded_recipe_file.write(ingredient.amount + " " + ingredient.description)

    secret_recipe_file.close()
    decoded_recipe_file.close()



if __name__ == "__main__":
    main()
