""" Workfile to be changed by the applicant """

import json
import requests
from selenium import webdriver


# Q1
# Add two ints, which come as white-space separated tokens in a string.

# Code fragment should be a function named q1, with sting as an input and sum returned.
# Any error should return string "err".


def q1(string_):
    try:
        return int(string_.split(" ")[0]) + int(string_.split(" ")[1])
    except:
        return "err"


# Q2
# Read a JSON from file, put into a dict, return
#   1) list of key-value tuples sorted by values (descending)
#   2) key of a pair which has a value of 5
#   3) value of a dict entry with key "two"

# Code fragment should be a function named q2, with string (filename) as an input and tuple (dict, int) returned.
# File-related errors should return "file_err", any other errors - "err"

# JSON in the input is supposed to be like this: {"key1": 1, "key": 2}


def q2(file_name):
    try:
        with open(file_name, "r") as file:
            try:
                json_data = json.loads(file.read())

                for item in json_data.items():
                    if item[1] == 5:
                        return sorted(json_data.items(), key=lambda item: item[1], reverse=True), \
                               item[0], \
                               json_data["two"]

            except:
                return "err"

    except:
        return "file_err"


# Q3
# Get a list of ints, remove all the items which are less than 10,
# return a CSV-string of the rest divided by 3 as floats with 2 decimals (like "3.66,4.00,4.3").

# Code fragment should be an annotated function named q3, with list as input and string returned.
# The caller should be able to modify the divider via optional argument (divider=string) defaulting to ","
# If there are no items in the resulting list, return null-object; any errors should return "err".


def q3(input_list: list, divider=",") -> str:
    try:
        output_list = [item / 3 for item in input_list if item >= 10]

        if len(output_list) > 0:
            return divider.join(["{0:.2f}".format(item) for item in output_list])
        else:
            return None  # lining error: return won't match the annotation, plus point if noticed

    except:
        return "err"


# Q4
# Define a URLGetter class, which inits with two instance variables:
# base_url (str, defaulting to 'https://swapi.co/api/people/') and params (dict, defaulting to {}).

# Code fragment should be a class named URLGetter, with relevant methods and attributes defined.
# Repr should return URL string formatted as '<URLGetter: https://url.com/?param=value>',
# class method get_body should return response body as JSON converted to dict.

class URLGetter():

    def __init__(self, base_url="https://swapi.co/api/people/", params={}):
        self.base_url = base_url
        self.params = params
        self.request = requests.get(base_url, params=self.params)

    def __repr__(self):
        return "<URLGetter: {}>".format(self.request.url)

    def get_body(self):
        return self.request.json()


# Q5
# Write a function which would grab the element text by URL and class name supplied

# Code fragment should be a function named q5, with URL and class name as inputs
# and element text returned as a string.
# Chrome webdriver is installed and should be used with Selenium.

def q5(url, class_name):
    with webdriver.Chrome() as driver:
        driver.get(url)
        elem = driver.find_element_by_class_name(class_name)
        return elem.text
