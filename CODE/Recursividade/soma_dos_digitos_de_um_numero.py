#**2. SOMA DOS DÍGITOS DE UM NÚMERO** (Fácil) — *novo*
#1. Defina a função: recebe um inteiro positivo `n`.
#2. Caso Base: se `n` tiver só um dígito (`n < 10`), retorne o próprio `n`.
#3. Recursão: retorne o último dígito (`n % 10`) somado à chamada da função com o restante do número (`n // 10`).
#- Complexidade: O(d), sendo d a quantidade de dígitos.

n = int(input("Digite um número com 1 dígito ou mais: "))
def soma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + soma_digitos(n // 10)