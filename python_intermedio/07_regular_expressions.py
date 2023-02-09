#Regular Expressions

import re
#match

my_string = "Esta es la leccion #7:\nLeccion llamadas Expresiones Regulares"
my_other_string = "Esta no es la leccion #6: Manejo de ficheros"

match = re.match("Esta es la leccion", my_string, re.I)

print(match)
start , end = match.span()
print(my_string[start:end])

match = re.match("Esta no es la leccion", my_other_string)
if match is not None:
    print(match)
    start,end = match.span()
    print(my_other_string[start:end])




print(re.match("Esta es la leccion", my_other_string))
print(re.match("Expresiones Regulares", my_string))


#search

search = re.search("leccion", my_string, re.I)
print(search)
start,end = search.span()
print(my_string[start:end])

#findall

findall = re.findall("leccion", my_string, re.I)
print(findall)

#split

print(re.split("\n", my_string))

#sub
print(re.sub("[l|L]eccion", "LECCION", my_string))
print(re.sub("Expresiones Regulares", "RegEx", my_string))


#patterns

pattern = r"[lL]eccion"
print(re.findall(pattern, my_string))

pattern = r"[lL]eccion|Expresiones"
print(re.findall(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))