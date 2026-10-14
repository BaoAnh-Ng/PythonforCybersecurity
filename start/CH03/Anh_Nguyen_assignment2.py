#!/usr/bin/env python3
# example workign with conditionals
#By me, 10/14

def send_message():
     print("Wonderful!") 

answer = input("Is today a good day, Anvie?")
if answer == "yes" or answer == "Yes":
   send_message()
else:
    print("Everything gonna be fine")

