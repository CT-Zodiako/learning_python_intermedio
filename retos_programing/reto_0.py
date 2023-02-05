# /*
#  * Escribe un programa que muestre por consola (con un print) los
#  * números de 1 a 100 (ambos incluidos y con un salto de línea entre
#  * cada impresión), sustituyendo los siguientes:
#  * - Múltiplos de 3 por la palabra "fizz".
#  * - Múltiplos de 5 por la palabra "buzz".
#  * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
#  */

numero = 0

while numero < 100:
    if numero % 3 == 0 and numero % 5 == 0:
        print(f"\nfizzbuzz {numero}")
    elif numero % 3 == 0:
        print(f"\nfizz {numero}")
    elif numero % 5 == 0:
        print(f"\nbuzz {numero}")
    numero += 1
