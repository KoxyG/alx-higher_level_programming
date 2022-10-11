#!/usr/bin/python3

def raise_exception():
    try:
        raise _exception()
    except TypeError:
        print("Exception raised")
        raise
