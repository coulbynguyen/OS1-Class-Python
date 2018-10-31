#!/usr/bin/python
from random import *


file1 = open("alpha.txt", "w")
file2 = open("tyler1.txt", "w")
file3 = open("gamma.txt", "w")
mystring = ""
mystring2 = ""
mystring3 = ""
x = randint(1,42)
y = randint(1,42)
product = x*y
for i in range(0,9):
   rand = randint(97,122)
   mystring += chr(rand)

for i in range(0,9):
   rand = randint(97,122)
   mystring2 += chr(rand)

for i in range(0,9):
   rand = randint(97,122)
   mystring3 += chr(rand)


file1.write(mystring + "\n")
file2.write(mystring2 + "\n")
file3.write(mystring3 + "\n")

print mystring
print mystring2
print mystring3
print x
print y
print product
