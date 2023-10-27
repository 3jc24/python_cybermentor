#!/bin/python3
###########################
# Cyber Mentor full video
###########################

x = float(input ("introduce numero: "))
o = input ("introduce operador: ")
y = float(input ("introduce otro numero: "))

if o == "+":
    print (x + y)

elif o == "-":
     print (x - y)

elif o == "*":
     print (x * y)

elif o == "/":
     print (x / y)

else:
    print ("Operador desconocido")