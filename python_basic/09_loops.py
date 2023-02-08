#loop 

#while

my_condition = 0

while my_condition  <10:
        print(my_condition)

        my_condition+=2
else:
    print("el while no se cumple")


#for

my_list = [1,3,4,5,6,7,6,5,4,3]
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
my_tuple = (24,1.63,"Cristian","Tovar")
my_other_set = {'Cristian', 'Tovar', 35}

for numero in my_list:
    print(numero)

for numero in my_other_dicht:
    print(numero)

for numero in my_other_dicht.values():
    print(numero)

for numero in my_tuple:
    print(numero)

for numero in my_other_set:
    print(numero)