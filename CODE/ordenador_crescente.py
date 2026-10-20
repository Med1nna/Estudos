def bubble_sort(lista):
    n = len(lista)
    # Percorre toda a lista
    for i in range(n):        
        # O final da lista já vai ficando ordenado, então o limite do loop diminui a cada iteração (n - i - 1)
            for j in range(0, n - i - 1):
            # Se o elemento atual for maior que o próximo...
                if lista[j] > lista[j + 1]:
                # ...executa o Swap (desempacotamento de tuplo)
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
numeros = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(bubble_sort(numeros)) # Resultado: [3, 4, 5, 8]