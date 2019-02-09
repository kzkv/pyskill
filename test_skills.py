""" pytest answers validator """

import pytest
import workfile
import dpath

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
    Q2 = [("q2_1.json", ([("tree", 1001), ("two", 202), ("one", 5)], "one", 202)),
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

    for test_item in Q3:
        if test_item[1] is None:
            print("input is '{}', with exected result '{}'".format(test_item[0], test_item[2]))
            assert workfile.q3(test_item[0]) == test_item[2]
        else:
            print(
                "input is '{}', divider is '{}', exected result '{}'".format(test_item[0], test_item[1], test_item[2]))
            assert workfile.q3(test_item[0], test_item[1]) == test_item[2]


# Q4: Classes and requests

# Class declaration and init
# Class repr
# requests, composing an URL
# requests, getting an object

@pytest.mark.q4
def test_q4():
    Q4 = [{"url": None,
           "params": {"search": "chew"},
           "path": "results/0/name",
           "lookup": "Chewbacca",
           "resulting_url": "https://swapi.co/api/people/?search=chew"},

          {"url": "https://swapi.co/api/people/1/",
           "params": {"format": "wookiee"},
           "path": "whrascwo",
           "lookup": "Lhuorwo Sorroohraanorworc",
           "resulting_url": "https://swapi.co/api/people/1/?format=wookiee"}]

    for test_item in Q4:
        if test_item["url"] == None:
            getter = workfile.URLGetter(params=test_item["params"])
            assert dpath.util.get(getter.get_body(), test_item["path"]) == test_item["lookup"]

        else:
            getter = workfile.URLGetter(base_url=test_item["url"], params=test_item["params"])
            assert dpath.util.get(getter.get_body(), test_item["path"]) == test_item["lookup"]

        assert getter.request.url == test_item["resulting_url"]
