
def get_num_words(text):
    
    word = len(text.split())

    return print(f"{word} words found in the document")


def bubble_sort(text):
    
    char = list(text)
    
    n = len(char)
    
    for i in range(n):
        for j in range(n-1):
            if char[j] > char[j+1]:
                temp = char[j]
                char[j] = char[j+1]
                char[j+1] = temp
                
    
