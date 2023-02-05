# /*
#  * Escribe una función que reciba dos palabras (String) y retorne
#  * verdadero o falso (Bool) según sean o no anagramas.
#  * - Un Anagrama consiste en formar una palabra reordenando TODAS
#  *   las letras de otra palabra inicial.
#  * - NO hace falta comprobar que ambas palabras existan.
#  * - Dos palabras exactamente iguales no son anagrama.
#  */

def words(word_one, word_two):

    if word_one.upper() == word_two.upper():
        return print(False)
    return print(sorted(word_one.upper())  == sorted(word_two.upper()))

words("Pala", "alpa")


