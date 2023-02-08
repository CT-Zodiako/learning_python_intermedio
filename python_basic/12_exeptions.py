#expetions

def name(uno,dos):
    print(f'suma {uno+dos}')

one = 2
two  = 2
try:
    name(one,two)
except:
    print("error")

#TRY EXCEPT ELSE
try:
    name(one,two)
except:
    print("error")
else:
    print('se ejecuta el else')

#TRY EXCEPT ELSE finaly
try:
    name(one,two)
except:
    print("error")
else:
    print('se ejecuta el else')
finally:
    print('Ejecucion finaly')

