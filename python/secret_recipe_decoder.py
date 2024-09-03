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
    # TODO: implement me
    decoded_string = ''
    for character in range(0, len(str)):
        if str[character] in ENCODING:
            decoded_char = ENCODING.get(str[character])
            decoded_string += decoded_char
        else:
            decoded_string += str[character]
    return decoded_string


def decode_ingredient(line):
    """Given an ingredient, decode the amount and description, and return a new Ingredient"""
    # TODO: implement me
    line_list = []
    if '#' in line:
        line_list = line.split('#', 1)
    decoded_amount = decode_string(line_list[0])
    decoded_ingredient = decode_string(line_list[1])
    return Ingredient(decoded_amount, decoded_ingredient)


def main():
    """A program that decodes a secret recipe"""
    # TODO: implement me

    secret_recipe_file = open("secret_recipe.txt", "r")
    decoded_recipe_file = open("decoded_recipe.txt", "w")

    decoded_ingredient_list = []

    secret_line = secret_recipe_file.readline()
    while secret_line:
        decoded_ingredient_list.append(decode_ingredient(secret_line))
        secret_line = secret_recipe_file.readline()

    secret_recipe_file.close()

    for ingredient in decoded_ingredient_list:
        decoded_recipe_file.write(ingredient.amount + " " + ingredient.description)

    decoded_recipe_file.close()

    test_decoded_file = open("decoded_recipe.txt", "r")
    print(test_decoded_file.read())



if __name__ == "__main__":
    main()
