""" Workfile to be changed by the applicant """

# Q1
# Add two numbers, which come as white-space separated tokens in a string
# Code fragment should be a function named q1, with sting as an input and sum returned
# Any error should return string "err"


def q1(string_):
    return string_.split(" ")[0] + string_.split(" ")[1]

# def q1(string_):
#     try:
#         return int(string_.split(" ")[0]) + int(string_.split(" ")[1])
#     except:
#         return "err"
