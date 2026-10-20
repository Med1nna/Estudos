#**1. CÁLCULO DE FATORIAL** (Fácil)
#1. Defina a função: recebe um inteiro `n`.
#2. Caso Base: se `n` for 0 ou 1, retorne 1.
#3. Recursão: se `n > 1`, retorne `n` multiplicado pela função(`n - 1`).
#- Complexidade: O(n).
#- Dica: desenhe a pilha de chamadas para `n = 4` no papel antes de codar; ajuda a visualizar onde a recursão "volta".

n = int(input("Digite um número: "))
def calculo_fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * (n - 1)

print(calculo_fatorial(n))