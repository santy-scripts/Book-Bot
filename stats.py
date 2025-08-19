def get_num_words(text):
    
    words = text.split(" ")

    return print(len(words))

def get_abc_words(text):
    
    abecedario = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]
    total_letras = 0
    contadorABC = {abc: 0 for abc in abecedario}  

    for palabra in text:
        if palabra != "":
            total_letras += len(palabra)
            for letra in palabra.lower():
                if letra in contadorABC:
                    contadorABC[letra] += 1 
                    
    for letra, cuenta in contadorABC.items(): 
        abcCount = print(f"{letra}: {cuenta}")

    return print(f"{abcCount}")


def bubble_sort(text):
    
    char = list(text)
    swapped = True
    n = len(char)
    
    while swapped:
        swapped = False
        for i in range(n):
            for j in range(n-1):
                if char[j] > char[j+1]:
                    temp = char[j]
                    char[j] = char[j+1]
                    char[j+1] = temp
                    swapped = True
        n -= 1
                
    return char
                
                
def get_num_letters(text):
    
    total_letras = 0

    for palabra in text:
        if palabra != "":
            total_letras += len(palabra)
            
    return print(f"{total_letras}")

    
