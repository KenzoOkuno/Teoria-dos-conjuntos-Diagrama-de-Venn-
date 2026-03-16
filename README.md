# Analisador de Conjuntos com Diagrama de Venn

Este repositório contém um script Python projetado para processar dados de entrada do usuário e realizar operações fundamentais da Teoria dos Conjuntos. O diferencial do projeto é a integração com bibliotecas gráficas para gerar um Diagrama de Venn proporcional e automatizado.

## Funcionalidades

O programa executa as seguintes operações lógicas e matemáticas:

* **União ($A \cup B$):** Agrupamento de todos os elementos presentes em ambos os conjuntos.
* **Interseção ($A \cap B$):** Identificação apenas dos elementos que pertencem simultaneamente a A e B.
* **Diferença ($A - B$ e $B - A$):** Isolamento dos elementos exclusivos de um conjunto específico.
* **Diferença Simétrica ($A \Delta B$):** Elementos que pertencem a A ou B, mas que não estão na área comum (interseção).
* **Visualização Gráfica:** Renderização de um diagrama de duas áreas com labels personalizadas.



## Tecnologias Utilizadas

O projeto foi desenvolvido utilizando:

1.  **Python 3**: Linguagem base para a lógica e manipulação de objetos do tipo `set`.
2.  **Matplotlib**: Biblioteca para a criação da interface gráfica e exibição do gráfico final.
3.  **Matplotlib-venn**: Extensão especializada na construção e cálculo de áreas para diagramas de Venn.

## Instalação e Pré-requisitos

Para executar este script localmente, você deve ter o Python instalado. As dependências externas podem ser instaladas via gerenciador de pacotes `pip` com o seguinte comando:

```bash
pip install matplotlib matplotlib-venn
