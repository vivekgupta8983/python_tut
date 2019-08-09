#!/bin/usr/python

import platform
import os
import sys

def get_platform():
    """Return the current OS platform.

    For example: if current os platform is Ubuntu then a string "ubuntu"
    will be returned (which is the name of the module).
    This string is used to decide which platform module should be imported.
    """
    tuple_platform = platform.dist()
    current_platform = tuple_platform[0]
    if "Ubuntu" in current_platform:
        print("ubuntu")
    elif "CentOS" in current_platform:
        print("centos")
    elif "Redhat" in current_platform:
        print(Redhat)
get_platform()
