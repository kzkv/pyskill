""" pytest answers validator """

import pytest
import workfile

# TODO: make a translator for adding/updating all the questions/tasks from datasource

# error descriptions
ERR_INPUT = "err"


# Q1: combine two ints from a string

# function declaration, input and output
# string manipulation
# str -> int coercion
# try/except or if/else wrapping

@pytest.mark.q1
def test_q1():
    Q1 = [("5 6", 11), ("1 20", 21), ("5.0 5", ERR_INPUT), ("9", ERR_INPUT), ("5+6", ERR_INPUT)]

    for pair in Q1:
        print("input is '{}', with exected result {}".format(pair[0], pair[1]))
        assert workfile.q1(pair[0]) == pair[1]


# Q2: read a JSON from file and manipulate the dict

# file reading
# closing file after use
# JSON to dict
# addressing dict entry by key
# sorting by value
# equal token (==)

@pytest.mark.q2
def test_q2():
    Q2 = [("q2_1.json", ([('tree', 1001), ('two', 202), ('one', 5)], 'one', 202)),
          ("q2_2.json", "err"),
          ("no_such_file.json", "file_err")]

    for pair in Q2:
        print("expected output is '{}' for the file '{}'".format(pair[1], pair[0]))
        assert workfile.q2(pair[0]) == pair[1]


# Q3: filter and manipulate list items

# function annotation
# optional params
# string formatting
# comparison
# map/filter or list comprehension
# list length
# None object

@pytest.mark.q3
def test_q3():
    Q3 = [([1, 5, 10, 15, 20], None, "3.33,5.00,6.67"),
          ([-1, 0, 1, 11, 12], "|", "3.67|4.00"),
          ([1, 2, 3], None, None),
          ([], None, None),
          ("input", None, "err")]

    for pair in Q3:
        if pair[1] is None:
            print("input is '{}', with exected result '{}'".format(pair[0], pair[2]))
            assert workfile.q3(pair[0]) == pair[2]
        else:
            print("input is '{}', divider is '{}', exected result '{}'".format(pair[0], pair[1], pair[2]))
            assert workfile.q3(pair[0], pair[1]) == pair[2]
