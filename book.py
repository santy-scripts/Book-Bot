import sys
from stats import (get_num_words, bubble_sort)

print(r"""  
 ____                    __                   
/\  _`\                 /\ \                  
\ \ \L\ \    ___     ___\ \ \/'\              
 \ \  _ <'  / __`\  / __`\ \ , <      _______ 
  \ \ \L\ \/\ \L\ \/\ \L\ \ \ \\`\   /\______\
   \ \____/\ \____/\ \____/\ \_\ \_\ \/______/
    \/___/  \/___/  \/___/  \/_/\/_/          
                                              
                                              
 ____                    __                   
/\  _`\                 /\ \__                
\ \ \L\ \    ___     ___\ \ ,_\               
 \ \  _ <'  / __`\  / __`\ \ \/               
  \ \ \L\ \/\ \L\ \/\ \L\ \ \ \_              
   \ \____/\ \____/\ \____/\ \__\             
    \/___/  \/___/  \/___/  \/__/                 
""")  

with open("book.txt", "r", encoding="utf-8") as f:
  
    text = f.read()

words = bubble_sort(text)
print(words)



"""  
   

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

"""