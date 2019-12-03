#!/usr/bin/env python3

import requests
from getpass import getpass


def fuel_calculation_for_modules_mass(mass):
    """Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a
        module, take its mass, divide by three, round down, and subtract 2."""

    fuel_calc = mass // 3 - 2
    print("fuel_calc : {}".format(fuel_calc))
    return fuel_calc


def fuel_counter_upper():
    """The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fuel
        needed for the mass of each module (your puzzle input), then add together all the fuel values.
        What is the sum of the fuel requirements for all of the modules on your spacecraft?"""
    # response = requests.get('https://adventofcode.com/2019/day/1/input', )
    # #with requests.get('https://adventofcode.com/2019/day/1/input', stream=True):
    # print("response.content : {}".format(response.content))
    # print("response.json: {}".format(response.json))

    with requests.Session() as session:
        session.auth = ('username', getpass())

        # Instead of requests.get(), you'll use session.get()
        response = session.get('https://adventofcode.com/2019/day/1/input')

    # You can inspect the response just like you did before
    print(response.headers)
    print(response.json())
    print("response.content : {}".format(response.content))

    # mass_dict = {}
    # with f = open('fuel.txt',"r"):
    #     print("readlines: {}".format(f.readlines())
    #     total_fuel_needed = [mass for mass in f.readlines()]
