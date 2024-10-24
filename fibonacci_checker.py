def is_in_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    if a == n:
        print(f"O número {n} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {n} não pertence à sequência de Fibonacci.")

# Solicita a entrada do usuário
numero = int(input("Informe um número: "))
is_in_fibonacci(numero)
