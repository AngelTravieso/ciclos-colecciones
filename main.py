# Ciclos

# Definir una lista de tipo str
# nombres = ['Juan', 'Karla', 'Ricardo', 'Maria']
#
# # Imprimir la lista de nombres
# print(nombres)
#
# # Acceder a los elementos de una lista
# print(nombres[0])
# print(nombres[1])
#
# # Acceder a los elementos de manera inversa
# print(nombres[-1])
# print(nombres[-2])
#
# # Imprimir un rango (sin incluir el 2do indice)
# print(nombres[0:2])
#
# # Ir del inicio de la lista al índice (sin incluirlo)
# print(nombres[:3])
#
# # Desde el índice indicado hasta el final
# print(nombres[1:])
#
# # Cambiar un valor de la lista
# nombres[3] = 'Ivone'
# print(nombres)
#
# # Iterar una lista
# for nombre in nombres:
#     print(nombre)
# else:
#     print('No existen más nombres en la lista')
#
#
# # Preguntar el largo de una lista
# print(len(nombres))
#
#
# # Agregar un elemento
# nombres.append('Lorenzo')
# print(nombres)
#
#
# # Insertar un elemento en un índice en específico
# nombres.insert(1, 'Octavio')
# print(nombres)
#
#
# # Remover un elemento (remueve por valor, no por índice)
# nombres.remove('Octavio')
# print(nombres)
#
#
# # Remover el último valor agregado a la lista
# nombres.pop()
# print(nombres)
#
#
# # Eliminar un elemento en un índice indicado
# del nombres[0]
# print(nombres)
#
#
# # Limpiar la lista
# nombres.clear()
# print(nombres)
#
#
# # Borrar la lista por completo
# del nombres
# print(nombres)


# Ejercicio: Iterar un rango de 0 a 10 e imprimir números divisibles entre 3

# contador = 1
#
# while contador <= 10:
#     contador += 1
#     if contador % 3 == 0:
#         print(contador)
# else:
#     print('Ciclo terminado')

# for contador in range(10):
#     if contador % 3 == 0:
#         print(contador)


# Tuplas (lista inmutable)

# Definir una tupla
# frutas = ('Naranja', 'Platano', 'Guayaba')
# print(frutas)
#
# # Saber la longitud de la tupla
# print(len(frutas))
#
# # Acceder a un elemento
# print(frutas[0])
#
# # Navegación inversa
# print(frutas[-1])
#
# # Acceder a un rango de valores
# print(frutas[0:2])
#
# # Recorrer elementos
# for fruta in frutas:
#     print(fruta, end=' ')
#
# # Cambiar el valor de una tupla
# # frutas[0] = 'Pera'
#
# frutasLista = list(frutas)
# frutasLista[0] = 'Pera'
# frutas = tuple(frutasLista)
# print('\n', frutas)
#
# # Eliminar la tupla
# del frutas
# print(frutas)


# Ejercicio: Tupla y Lista

# numeros = (13, 1, 8, 3, 2, 5, 8)
# numerosLista = []
#
# for numero in numeros:
#     if numero < 5:
#         numerosLista.append(numero)
#
# print(numerosLista)


# Set en Python
# planetas = {'Marte', 'Jupiter', 'Venus'}
# print(planetas)
#
# # longitud de set
# print(len(planetas))
#
# # Revisar si un elemento está presente
# print('Marte' in planetas)
#
# # Agregar un elemento
# planetas.add('Tierra')
# print(planetas)
#
# # No se pueden duplicar elementos
# # Solo agregará 1 valor si está repetido
# planetas.add('Tierra')
# print(planetas)
#
# # Eliminar elemento
# planetas.remove('Tierra')
# print(planetas)
#
# # Sirve para eliminar, pero no arroja excepción en caso de que no encuentre
# # el elemento
# planetas.discard('Jupiter')
#
# # Limpiar set
# planetas.clear()
# print(planetas)
#
# # Eliminar set
# del planetas
# print(planetas)


# Diccionarios (key, value)

diccionario = {
    'IDE': 'Integrated Development Environment',
    'OOP': 'Object Oriented Programming',
    'DBSM': 'Database Management System'
}

print(diccionario)

# Longitud diccionario
print(len(diccionario))

# Acceder a un elemento en especiífico
print(diccionario['IDE'])

# Otra forma de recuperar un elemento
print(diccionario.get('OOP'))

# Modificando elementos
diccionario['IDE'] = 'integrated development environment'
print(diccionario)

# Recorrer los elementos
for termino, valor in diccionario.items():
    print(termino, valor)

# Recuperar solo las llaves
for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)

# Comprobar existencia de algún elemento
print('IDE' in diccionario)

# Agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

# No es posible duplicar elementos en un diccionario

# Remover un elemento
# diccionario.pop('DBMS')
# print(diccionario)

# Limpiar diccionario
diccionario.clear()
print(diccionario)

# Eliminar diccionario
del diccionario
print(diccionario)



