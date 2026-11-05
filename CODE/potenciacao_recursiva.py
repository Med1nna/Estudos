#**4. POTENCIAÇÃO RECURSIVA** (Médio)
#1. Defina a função: recebe `base` e `expoente`.
#2. Caso Base: se `expoente == 0`, retorne 1.
#3. Recursão: se `expoente > 0`, retorne `base` multiplicada pela função(`base`, `expoente - 1`).
#- Complexidade: O(n) na versão simples.
#- Desafio extra: implemente a exponenciação rápida, dividindo o expoente por 2 a cada chamada em vez de subtrair 1 — cai para O(log n).

numero = int(input("Insira o número que será elevado a potência:\n"))
potenciacao = int(input("Insira a potência:\n"))


def potenciacao_recursiva(base, expoente):
    if expoente == 0:
        #expoente = 1
        return 1
    else:
        return base * potenciacao_recursiva(base, expoente - 1)
        #resultado = base**expoente
    #return resultado

print(potenciacao_recursiva(numero, potenciacao))