def palindrome(x):
  x=x.lower()
  resultado = x[::-1] == x
  return resultado

word1= input("Escriba la palabra que quieres saber si es palíndrome: ")
resultado=palindrome(word1)

if resultado== True:
  print("¡Si!, ¡La palabra es palíndrome")
else:
  print("Desgraciadamente, la palabra no es palíndrome")