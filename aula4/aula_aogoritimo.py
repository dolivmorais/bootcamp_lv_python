lista_denumeros = [1, 2, 3, 455, 6, 7, 8, 9, 10]

b = lista_denumeros.sort()
print(b)

def bubble_sort(lista):
    nova_lista = lista.copy()
    
    for i in range(len(nova_lista)):
        for j in range(i + 1, len(nova_lista)):
            if nova_lista[i] > nova_lista[j]:
                aux = nova_lista[i]
                nova_lista[i] = nova_lista[j]
                nova_lista[i], nova_lista[j] = nova_lista[j], nova_lista[i]

    return nova_lista


a = bubble_sort(lista_denumeros)
print(a)

