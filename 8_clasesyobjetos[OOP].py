#!/bin/python3
###########################
# Cyber Mentor full video
###########################

# definimos la clase empleado junto con sus metodos (funciones)
class Employees:
    def __init__(self, name, department, role, salary, years_employed):
        self.name = name
        self.deparment = department
        self.role = role
        self.salary = salary
        self.years_employed = years_employed

    def jubilacion(self):
        return self.years_employed >= 20


# creamos objetos de la clase empleado
e1 = Employees ("EJ", "IT", "Sysadmin", "100000", 21)
e2 = Employees ("Tom", "IT", "Developper", "1000", 9)

print (e1.name)
print (e1.role)
print (e2.name)
print (e2.role)

# llamadas al metodo jubilacion para los 2 objetos
print (e1.jubilacion())
print (e2.jubilacion())