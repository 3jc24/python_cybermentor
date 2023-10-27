#!/bin/python3
###########################
# Cyber Mentor full video
###########################

# Read file
file = open ("meses.txt", "r")
print (file)
print (file.read())
file.close()

# Read line by line
file = open ("meses.txt", "r")
print (file.readline())
print (file.readline())
file.close()

# Read line by line an put into a list
file = open ("meses.txt", "r")
print (file.readlines())
file.close()

# Read with a loop
file = open ("meses.txt", "r")
for mes in file:
    print (mes.strip())
file.close()

# write on a new file
file = open ("days.txt", "w")
file.write ("Lunes")
file.close()

# append to a new file
file = open ("days.txt", "a")
file.write ("\nMartes")
file.close()


# Read again
file = open ("days.txt", "r")
print (file.read())
file.close()