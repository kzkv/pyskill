""" pytest answers validator """

import pytest
import workfile

# TODO: make a translator for adding/updating all the questions/tasks from datasource

# error descriptions
ERR_INPUT = "err"


# Q1: combine two numbers from a string
@pytest.mark.q1
def test_q1():
    Q1 = [("5 6", 11), ("1 20", 21), ("9", ERR_INPUT), ("5+6", ERR_INPUT)]

    for pair in Q1:
        print("input is '{}', with exected result {}".format(pair[0], pair[1]))
        assert workfile.q1(pair[0]) == pair[1]


# Q2: some other task for marker demonstration
@pytest.mark.q2
def test_q2():
    Q1 = [("5 6", 11), ("1 20", 21), ("9", ERR_INPUT), ("5+6", ERR_INPUT)]

    for pair in Q1:
        print("input is '{}', with exected result {}".format(pair[0], pair[1]))
        assert workfile.q2(pair[0]) == pair[1]
