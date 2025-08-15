
print("""    
__________               __               __________ ___________________
\______   \ ____   ____ |  | __           \______   \\_____  \__    ___/
 |    |  _//  _ \ /  _ \|  |/ /   ______   |    |  _/ /   |   \|    |   
 |    |   (  <_> |  <_> )    <   /_____/   |    |   \/    |    \    |   
 |______  /\____/ \____/|__|_ \            |______  /\_______  /____|   
        \/                   \/                   \/         \/         
      """)


phrase = input("Enter a Phrase: ")
word = phrase.split(" ")
abecedario = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

def book():
    total_letras = 0
    contadorABC = {abc: 0 for abc in abecedario}  

    for palabra in word:
        if palabra != "":
            total_letras += len(palabra)
            for letra in palabra.lower():
                if letra in contadorABC:
                    contadorABC[letra] += 1 
                    
                    
    print("============ BOOKBOT ============")
    print(f"----------- Word Count ----------")
    print(f"{len(word)}")
    print(f"--------- Character Count -------")
    print(f"{total_letras}")
    print(f"-------- Count per Letter -------")
    for letra, cuenta in contadorABC.items(): 
        print(f"{letra}: {cuenta}")
    print("============= END ===============")

book()

