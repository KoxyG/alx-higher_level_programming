#!/usr/bin/python3

def raise_exception_msg(message=""):
    try:
        raise NameError("Hi, its Koxy :)")
    except NameError:
        print("There was an exception")
        raise
