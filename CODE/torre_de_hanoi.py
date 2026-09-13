#**6. TORRE DE HANÓI** (Difícil)
#1. Defina a função: precisa de `n` discos e três pinos (origem, destino, auxiliar).
#2. Caso Base: se `n = 1`, mova da origem para o destino e encerre.
#3. Primeira Recursão: se `n > 1`, mova `n-1` discos da origem para o auxiliar.
#4. Ação Principal: mova o maior disco da origem para o destino.
#5. Segunda Recursão: mova os `n-1` discos do auxiliar para o destino.
#- Complexidade: O(2^n) movimentos — é o mínimo matematicamente necessário.

n_discos = int(input("Digite o número de discos: "))

# Representação das torres como listas (pilhas)
# O maior disco fica na base (início) e o menor no topo (fim da lista)
torre_1 = list(range(n_discos, 0, -1))
torre_2 = []
torre_3 = []

def exibir_torres():
    print(f"Torre 1: {torre_1}")
    print(f"Torre 2: {torre_2}")
    print(f"Torre 3: {torre_3}")
    print("-" * 35)

def torre_de_hanoi(n, origem, destino, auxiliar, nome_origem, nome_destino, nome_auxiliar):
    # 2. Caso Base: se n = 1, mova da origem para o destino e encerre.
    if n == 1:
        disco = origem.pop()
        destino.append(disco)
        print(f"\nMovendo disco {disco}: {nome_origem} -> {nome_destino}")
        exibir_torres()
        return

    # 3. Primeira Recursão: se n > 1, mova n-1 discos da origem para o auxiliar.
    torre_de_hanoi(n - 1, origem, auxiliar, destino, nome_origem, nome_auxiliar, nome_destino)

    # 4. Ação Principal: mova o maior disco da origem para o destino.
    disco = origem.pop()
    destino.append(disco)
    print(f"\nMovendo disco {disco}: {nome_origem} -> {nome_destino}")
    exibir_torres()

    # 5. Segunda Recursão: mova os n-1 discos do auxiliar para o destino.
    torre_de_hanoi(n - 1, auxiliar, destino, origem, nome_auxiliar, nome_destino, nome_origem)

print("\n--- Estado Inicial ---")
exibir_torres()

torre_de_hanoi(n_discos, torre_1, torre_3, torre_2, "Torre 1", "Torre 3", "Torre 2")

print(f"Total de movimentos realizados: {2**n_discos - 1}")