def fibonacci(n):
    sequencia = [0, 1]
    while sequencia[-1] < n:
        proximo = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo)
    
    print(f"Sequência de Fibonacci: {sequencia}")

    if n in sequencia:
        print(f"O número {n} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {n} não pertence à sequência de Fibonacci.")

fibonacci(100)