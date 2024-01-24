
text = "Hola a todos, esta es una cadena de texto de prueba."
print(text)
unique = { c: text.count(c) for c in text if c in 'aeiou' }
print(f"unique: {unique}")

