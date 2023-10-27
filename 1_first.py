###########################
# Cyber Mentor short video
###########################

# strings
print ("Hello, World")
print ("""HOLA
MUNDO 
MUNDO"""+ "\n" + """MUNDO2
MUNDO3""")

# Matematicos
print (50 / 6)
print (50 // 6)
print (50 % 6)

# Avariables
hola = "Hola mundo"
print (hola)

# Methods
# Mini programs
# buildin programs

print (hola.upper())
print (hola.lower())
print (hola.title())
print (len(hola))

# Numbers
name = "Jesus"
age = 44 # integer
gpa = 3.7 # float - with decimals


print (int(age))
print (int(gpa))
print (int(3.1))
print (int(3.9))
print (round(3.9))

print ("My name is " + name + " and I am " + str(age) + " years old" )

# functions with parameters
def who_am_i (name1:str, age1:int):
    print ("My name is " + name1 + " and im " + str(age1) + " years old.")

who_am_i ("john", 33)


# Other functions
# La raiz cudrada es la potencia de 0.5
def raiz_cuadrada (numero:int):
    return (numero ** 0.5)

print (raiz_cuadrada(23))

# Boolean Expressions

verdadero = 3*3==9
if verdadero:
    print ("verdadero")
else:
    print (verdadero)


# Listas y Bucles
print ("\n")
print ("Listas y Bucles")

lista = ['30 monedas','The morning show','Lupin']
print (lista[1])
lista.append('The beast')
print (len(lista))
print ("\n")

# listado de elementos de una lista
for i in range(0,len(lista)):
    print (i)
    print(lista[i])

# vaciado de lista
# sacando elementos desde el final con "pop"
for i in range(0,len(lista)):
    print (lista.pop())

# lista vacia desde de sacar elementos
print (lista)

   


    







