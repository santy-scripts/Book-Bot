phrase = input("ingrese una frase: ")
word = phrase.split(" ")
abecedario = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

# script
def book():

    contador = 0
    contadorABC = 0

    for palabra in word:

        if word != " ":
            contador += len(palabra)

        totalLetras = print(f"total de letras encontradas", contador)

        for letra in palabra:

            for abc in abecedario:

                if abc == letra:
                    contadorABC += 1

                totalABC = print(f"{abc}: {contadorABC}")

    totalPalabras = print(f"total de palabras encontradas es {len(word)}")

    return totalABC, totalLetras, totalPalabras


book()
