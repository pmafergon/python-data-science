import string

sentence = input("Agregue la frase que quiere saber si es palíndroma, como por ejemplo: Anita lava la tina: ")
abcd = string.ascii_letters

def palindr(x):
    y = ''.join(i for i in x if i in abcd)
    print(y)
    result = y.lower() == y.lower()[::-1]
    return result

result = palindr(sentence)
if result:
    print("¡La frase es palíndroma!")
else:
    print("La frase no es palíndroma")
