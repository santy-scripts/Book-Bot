phrase = input("ingrese una frase: ")  
word = phrase.split(" ")  
    
def allLetter(contador):
     
    contador = 0

    for i in word:     
        if word != " ":
            contador += len(i)
            
    return print(f"total de letras encontradas", contador)
    
def charCount():  
    
    return print(f"total de palabras encontradas es {len(word)}")
 
def searchLetter():
    
    letras = ["a", "e", "i", "o", "u"]
    contador = 0
    
    for i in word:
        for l in i:
            for n in letras:
                if l == n:
                    contador += 1
                    
                resul = print(f"el numero de letras {l} es {contador}")
                
     
    return resul
    
    
#allLetter(0)
searchLetter()

    



    