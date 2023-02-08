#File Handling
import os
# .txt file

txt_file = open("learning_python/python_intermedio/my_file.txt","w+")
txt_file.write("Mi nombre es Cristian\nMi apellido es Tovar\n24 años\nY mi lenguaje preferido es Python")


# print(txt_file.read())
# print(txt_file.read(30))
# print(txt_file.readline())
# print(txt_file.readlines())

for line in txt_file.readlines():
    print(line)
    
txt_file.write("\nme gusta la rumba")
print(txt_file.readlines())

txt_file.close()

# os.remove("learning_python/python_intermedio/my_file.txt")\
    
# .json file
import json

json_file = open("learning_python/python_intermedio/my_file.json","w+")

json_test = {
    "nombre" : "Cristian",
    "apellido" : "Tovar",
    "edad" : 24,
    "lenguage": ["Python","Java","JavaScript"],
    "website": "https://www.youtube.com/watch?v=TbcEqkabAWU&list=PLNdFk2_brsRdgQXLIlKBXQDeRf3qvXVU_&index=2"
}

json.dump(json_test, json_file, indent=4)

json_file.close()

with open("learning_python/python_intermedio/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)
        
json_dict = json.load(open("learning_python/python_intermedio/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["nombre"])

# .csv file
import csv



# .xlsx file
import xlrd #install module

# .xml file
import xml



