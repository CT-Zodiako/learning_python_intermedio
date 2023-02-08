#Error types

#SyntaxError
# print "Hola"
print("Hola")

#NameError
# print(name)
name = 'Cristian'
print(name)

#IndexError
my_list = ['Python', 'Kotlin',"Dart"]
# print(my_lisy[4])
print(my_list[2])

#ModuleNotFoundError
# import maths
import math

#AttributeError
# print(math.PI)
print(math.pi)

#KeyError
my_dict = {
    "nombre":"Cristian",
    "apellido": "Tovar"
}
# print(my_dict["edad"])
print(my_dict["apellido"])

#TypeError
# print(my_list["nombre"])
print(my_list[0])

#ImportError
# from math import PI
from math import pi
print(pi)

# ValueError
# my_int = int("10 años")
my_int = int("10")
print(type(my_int))

#ZeroDivisionError
# print(10/0)
print(10/2)



