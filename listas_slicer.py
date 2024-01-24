
#versión 1
'''sentence="Escriba una función que utilice slices para extraer las palabras que están en las posiciones impares de una frase"
sentence= sentence.split()
print(sentence)
def noPar(x):
    y=[]
    for i,word in enumerate(x):
        if i % 2 == 0:
            y.append(word)
    return y

result=noPar(sentence)
print(result)
'''
#list comprehension
sentence="Escriba una función que utilice slices para extraer las palabras que están en las posiciones impares de una frase"
sentence= sentence.split()
print(sentence)
def noPar(x):
    y=[word for i,word in enumerate(x) if i%2==0]
    return y

result=noPar(sentence)
print(result)
