def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    contadorDeLetras = cantidadDeLetras(text.split())
    listadoDeLetras = pasarDiccionarioALista(contadorDeLetras)
    for letra in listadoDeLetras:
        caracter = letra[0]
        cantidad = letra[1]
        print(f"The '{caracter}' character was found {cantidad} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def cantidadDeLetras(texto):
    contador = {}
    for palabra in texto:
        palabraEnMinuscula = palabra.lower()
        for car in palabraEnMinuscula:
            if car in contador:
                contador[car] += 1
            else:
                contador[car] = 1
    return contador 

def pasarDiccionarioALista(diccionario):
    lista_resultante = [(caracter, cantidad) for caracter, cantidad in diccionario.items()]
    lista_resultante.sort(key=lambda x: x[1], reverse=True)
    return lista_resultante

main()