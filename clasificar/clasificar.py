# Clasifica las palabras de una oracion de manera alfabetica

# Pedir datos
oracion = input("Ingresa una oración larga con espacios: ")

# Convirtiendo la oración en una lista de palabras
words = [word.lower() for word in oracion.split()]

# Ordena la lista
words.sort()

# Muestra las palabras clasificadas
print("Las palabras clasificadas alfabeticamente son:")
for word in words:
   print(word)
