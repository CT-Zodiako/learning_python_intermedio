my_string = "Mi string"
my_other_string = "Otro\nstring"
my_other_string_tabulation = "\tOtro string tabulado"

print(len(my_string));
print(my_other_string);
print(my_other_string_tabulation);

#formateo
name, surname, edad = 'Cristian' , 'Tovar', 24;

print("mi nombre es {} {} y mi edad es {}".format(name,surname,edad))
print("mi nombre es %s %s y mi edad es %d"%(name,surname,edad))
print(f"mi nombre es {name} {surname} y mi edad es {edad}")

#desempaquedatos de string
language = 'Python'
a, b, c, d, e, f =  language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#division 
language_slice = language[1:3]
print(language_slice)
language_slice = language[1:]
print(language_slice)
language_slice = language[:3]
print(language_slice)
language_slice = language[-1]
print(language_slice)
reversed_language = language[0:6:2]
print(reversed_language)

#reverse
reversed_language = language[::-1]
print(reversed_language)

#Funciones methods
print(len(reversed_language))
print(language.capitalize())
print(language.upper())
print(language.count('t'))
print(language.isnumeric())
print("5".isnumeric())








