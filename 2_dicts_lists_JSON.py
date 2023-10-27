#!/bin/python3
###########################
# Cyber Mentor full video
###########################

# Algo de matematicas simples 
# division en float pasada a entera
print (int(50/50))

########################
# VARIABLES AND METHOD
########################
print ("\n")
frase = "Esto es una prueba"
print (frase.upper())
print (frase.lower())
print (frase.title())

#######################
# FUNCTIONS
#######################
def funcion():
    print ("Hola")

funcion()

def nl():
    print ("\n")

nl()

# TUPLAS Y BUCLES
# diferencia entre lista y tupla :
# la tupla no se puede modificar

tupla = ("piedra", "papel", "tijera")
for i in tupla:
    print (i)


# bucles while
nl()
a=1
while a <= 10:
    print (a)
    a +=1


# Advance Strings
nl()
x = "Esto es una prueba"
print (x[:6])
print (f"{x}") #Only in python3


# Dictionaries
# key/valiue pairs
# JSON FORMATS
nl()

users = [ 
    {
        "name": "EJ",
        "age": 44,
        "email": ["sdsds@terra.es", "sdsdsd@terra.es"],
    },
    {
        "name": "Ron",
        "age": 33,
        "email": "sdsdfdds@terra.es"
    },
    {
        "name": "john",
        "age": 57,
        "email": "sdsdfdds@terra.es"
    }
]

print (type(users))
print (len(users))
nl()
print (users[0])
nl()

def nombres (lista):
    for i in range(0,len(lista)):
        print (users[i]["name"])

nombres (users)

nl()
def edades (lista):
    for i in range(0,len(lista)):
        print (users[i]["age"])

edades(users)

def correos (lista):
     for i in range(0,len(lista)):
        print ("****** email *****\n")
        print (users[i].get("email"))

correos (users)

def it (lista):
     for i in range(0,len(lista)):
        users[i].update({"department": "IT"})

it (users)

print (users)

# añadimos un año a cada usuario
def cumple (lista):
    for i in range(0,len(lista)):
        users[i]["age"] += 1

cumple (users)
edades (users)