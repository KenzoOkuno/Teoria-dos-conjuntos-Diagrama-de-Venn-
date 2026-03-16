from matplotlib import pyplot as plt
from matplotlib_venn import venn2

# função para converter texto em conjunto
def ler_conjunto(nome):
    entrada = input(f"Digite os elementos do conjunto {nome} separados por espaço: ")
    return set(map(int, entrada.split()))

while True:

    # ler conjuntos
    A = ler_conjunto("A")
    B = ler_conjunto("B")

    # operações de conjuntos
    uniao = A | B
    intersecao = A & B
    A_menos_B = A - B
    B_menos_A = B - A
    dif_simetrica = A ^ B

    # mostrar resultados
    print("\nResultados:")
    print("A =", A)
    print("B =", B)
    print("União (A ∪ B):", uniao)
    print("Interseção (A ∩ B):", intersecao)
    print("A - B:", A_menos_B)
    print("B - A:", B_menos_A)
    print("Diferença Simétrica:", dif_simetrica)

    # desenhar diagrama
    plt.figure(figsize=(6,6))
    venn2([A, B], set_labels=('A', 'B'))
    plt.title("Diagrama de Venn")
    plt.show()

    # perguntar se o usuário quer continuar
    continuar = input("\nDeseja fazer outro cálculo? (s/n): ").lower()

    if continuar != 's':
        print("Programa encerrado.")
        break