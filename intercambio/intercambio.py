# Programa para cambiar valor de dos variables enteras

# Recoge datos de usuario
x = input('Ingresa el valor de x: ')
y = input('Ingresa el valor de y: ')

print('El valor actual de x es: ', x)
print('El valor actual de y es: ', y)

# Creacion de variable temporal e intercambia valor con temp
temp = x
x = y
y = temp

print('El valor de x despues de intercambiar es: {}'.format(x))
print('El valor de x despues de intercambiar es: {}'.format(y))