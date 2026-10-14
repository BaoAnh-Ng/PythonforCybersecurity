#!/usr/bin/env python3
# Sample script that reads from a file
# By me, 10/14

import os
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

file_path = os.path.join(script_dir, "hackme.txt")
print("Here is someone to hack - information")

f = open(file_path, "r")

content = f.read()
print(content)

f.close()
