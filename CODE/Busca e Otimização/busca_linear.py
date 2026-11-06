lista = []
n_itens = int(input("Digite o número de itens da lista : "))
while len(lista) < n_itens:
    item = input("Digite o item que será inserido na lista: ")
    if item not in lista:
        lista.append(item)
    else:
        print("Esse item já foi inserido na lista, digite outro item.")
item_procurado = input("Digite o item que deseja buscar na lista: ")
def busca(lista, item_procurado):
    if  item_procurado not in lista:
        print(f"O item procurado ({item_procurado}) não está na lista." )
        return -1
    else:
        for i in range(len(lista)):
            if lista[i] == item_procurado:
                print(f"O item procurado ({item_procurado}) está na lista, na posição {i+1}.")
                break
                
busca(lista, item_procurado)