n = int(input("Insira qual posição você deseja saber da sequência de Fibonacci que deseja saber: "))
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
print(f"O {n}º número da sequência de Fibonacci é: {fibonacci(n)}")