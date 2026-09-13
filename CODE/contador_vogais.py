palavra = input("Digite uma palavra: ").lower
contador = 0
vogais = "aeiou"


for letra in palavra:
    if letra in vogais:
        contador += 1

print(f"A palavra {palavra} possui {contador} vogal(is).")