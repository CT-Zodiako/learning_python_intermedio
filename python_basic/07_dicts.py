#Diccionaries

my_dict = dict()

my_other_dicht = {}

my_other_dicht = {
    "nombre" : "Cristian",
    "apellido" : "Tovar",
    "edad" : 24,
    "Lenguage" : {"Python","Swift", "Kotlin"},
    1: {
        "color" : "rojo",
        "comida" : "lasanga"
    }
}

print(my_other_dicht)

print(len(my_other_dicht))

print(my_other_dicht["nombre"])
print(my_other_dicht["Lenguage"])

print(my_other_dicht.items())
print(my_other_dicht.keys())
print(my_other_dicht.values())

my_new_dict = dict.fromkeys(my_other_dicht)
print(my_new_dict)

my_new_dict = dict.fromkeys(my_other_dicht , None)
print(my_new_dict)