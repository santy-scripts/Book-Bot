
        
def searchLetter(contador):
    phrase = input("ingrese una frase: ")
    word = phrase.split(" ")    
    contador = 0

    for i in word:     
        if word != " ":
            contador += len(i)
            
    return print(f"total de letras encontradas", contador)
    
def charCount():
    phrase = input("ingrese una frase: ")
    word = phrase.split(" ")    
    
    
    return print(f"total de palabras encontradas es {len(word)}")
    
    
#searchLetter(0)

charCount()

    



    