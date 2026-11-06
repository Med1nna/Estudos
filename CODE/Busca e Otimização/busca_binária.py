lista = [1,2,3,4,5,6,7,8,9,10]
item_procurado = 7
def busca_binaria(lista,item_procurado):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = fim // 2
        if meio == item_procurado:
            print (meio)
            return meio
        elif meio < item_procurado:
            fim = meio - 1
        elif meio > item_procurado:
            inicio = meio + 1
busca_binaria(lista,item_procurado)