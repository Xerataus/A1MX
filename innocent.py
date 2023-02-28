
import os 

'''
 
Some secret code here:
  Example:
    os.system("rm -rf important")

'''

print("Revoke Access To Fragile Code")

with open(os.path.realpath(__file__), "w") as this_one:
  this_one.write("print(\"Revoke Access To Fragile Code\")")
