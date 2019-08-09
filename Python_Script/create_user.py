#!/usr/bin/python

import os
import crypt

name = input("Enter the Your Name:")
username = input("%s Enter your username:" % (name))
password = input("%s Enter your Password:" % (name))
def createuser():
    encPass = crypt.crypt(password,"22")
    return os.system("sudo useradd -p "+encPass+ " -s "+ "/bin/bash "+ "-d "+ "/home/" + username+ " -m "+ " -c \""+ name+"\" " + username)
    return os.system("sudo usermod -a -G sudo "+username)
createuser()


