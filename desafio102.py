def fatorial(n, show=True):
    """
    Calcula o fatorial de um número.

    :param n: Número para calcular o fatorial (deve ser inteiro e não negativo)
    :param show: (opcional) Exibe o processo do cálculo se True
    :return: O valor do fatorial de n
    """
    if n < 0:
        return "Fatorial não é definido para números negativos."
    
    resultado = 1
    for i in range(n, 0, -1):
        if show:
            print(f"{i} {'x' if i > 1 else '='} ", end="")
        resultado *= i
    if show:
        print(resultado)
    return resultado

a = int(input("Informe o número: "))
print(f"Fatorial de {a} é {fatorial(a)}")

