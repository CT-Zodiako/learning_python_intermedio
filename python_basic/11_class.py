#class

# class Person:
#     nombre = str
#     apellido = str

#     def say_your_name(name , apellido):
#         return (f"{name} {apellido}")


# firts_person = Person
# name = firts_person.nombre = 'Cristian'
# surname = firts_person.apellido = 'Tovar'


# print(firts_person.say_your_name(name , surname))



class Person_two:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def name_year(self):
        print(f"{self.name},{self.age}")

my_person_two = Person_two('Cristian', 'Tovar', 24)
my_person_two.name_year()