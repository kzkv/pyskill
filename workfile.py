""" Workfile to be changed by the applicant """

import json


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
            return None

    except:
        return "err"

