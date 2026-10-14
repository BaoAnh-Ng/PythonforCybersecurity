#!/usr/bin/env python3
# Sample script that writes to a file
# By me, 10/14

import os
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

file_path = os.path.join(script_dir, "hackme.txt")

name = input("What is your name? ")
color = input("What is your favorite color? ")
pet = input("What was your first pet's name? ")
maiden_name = input("What is your mother's maiden name? ")
school = input("What elementary school did you attend? ")

f = open(file_path, "w")

f.write("My name is Bao Anh(Anvie) \n")
f.write("My favourite color is emerald green \n")
f.write("Her name is Mun \n")
f.write("It's Dang \n")
f.write("Pascal International School \n")

f.close()
