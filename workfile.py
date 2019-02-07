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


print(q2("q2_1.json"))
