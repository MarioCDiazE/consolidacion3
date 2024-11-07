nombres = ['Harry Houdini', 'Newton', 'David Blaine', 'Hawking', 'Messi', 'Teller', 'Einstein', 'Pele', 'Juanes']

def separar_grupos(nombres):
    magos = []
    cientificos = []
    otros = []
    
    for nombre in nombres:
        if nombre in ['Harry Houdini', 'David Blaine', 'Teller']:
            magos.append(nombre)
        elif nombre in ['Newton', 'Hawking', 'Einstein']:
            cientificos.append(nombre)
        else:
            otros.append(nombre)
    
    return magos, cientificos, otros

def hacer_grandioso(magos):
    for i in range(len(magos)):
        magos[i] = 'El gran ' + magos[i]

def imprimir_nombres(nombres):
    for nombre in nombres:
        print(nombre)

magos, cientificos, otros = separar_grupos(nombres)

hacer_grandioso(magos)
print("\n")

print("Nombres de los magos grandiosos:")
imprimir_nombres(magos)
print("\n")

print("Nombres de los científicos:")
imprimir_nombres(cientificos)
print("\n")

print("Otros nombres:")
imprimir_nombres(otros)
print("\n")

print("Lista completa de nombres:")
imprimir_nombres(nombres)