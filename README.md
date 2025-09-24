# Olimpíada Brasileira de Informática

---
Modalidade Programação
Na Modalidade Programação, competidores fazem as provas no computador, com tarefas de programação que podem ser resolvidas com uma linguagem de programação entre Python, C, C++, Java e Javascript. Os níveis são:

## MEU NÍVEL NA COMPETIÇÃO:
Nível Sênior, para alunos do 4º ano do Ensino Técnico e alunos cursando pela primeira vez o 1º ano de um curso de graduação.

### Linguagem Escolhida: PYTHON


### Exemplos (uso)
Excelente ideia\! Entender cada componente é fundamental.
Vamos criar uma "mini-tabelinha" com os comandos e conceitos mais comuns e importantes em Python para quem está começando na OBI, focando em como eles funcionam e para que servem.

-----

### **Comandos e Conceitos Essenciais para OBI em Python**

| Comando/Conceito | Descrição | Exemplo de Uso | Para que Serve na OBI |
| :--------------- | :-------- | :------------- | :-------------------- |
| `import sys` | Importa o módulo `sys`, que fornece acesso a variáveis e funções que interagem fortemente com o interpretador Python. | `import sys` | Essencial para usar `sys.readline()` para leitura de entrada **rápida**, importante em problemas com muitos dados. |
| `input()` | Lê uma linha de texto da entrada padrão (teclado) e retorna como uma string. | `nome = input()` | Para entradas pequenas ou quando a velocidade não é crítica. Geralmente **evitado na OBI** para entradas grandes. |
| `sys.readline()` | Lê uma linha de texto da entrada padrão (teclado/arquivo) de forma mais eficiente que `input()`. Retorna uma string que **inclui o caractere de nova linha (\\n)**. | `linha = sys.readline()` | **Altamente recomendado na OBI** para ler entradas, especialmente quando há muitas linhas ou linhas longas, devido à sua velocidade. |
| `int()` | Converte um valor (geralmente string) para um número inteiro. | `num = int("123")` <br> `n = int(sys.readline())` | Para converter a entrada de texto (lida por `input()` ou `sys.readline()`) em números que podem ser usados em cálculos. |
| `float()` | Converte um valor para um número de ponto flutuante (com casas decimais). | `preco = float("19.99")` | Usado quando o problema envolve números não inteiros. |
| `str()` | Converte um valor para uma string (texto). | `texto = str(123)` | Útil para concatenar números com textos ou para formatar a saída. |
| `.split()` | Um método de string que divide a string em uma lista de substrings. Por padrão, divide por espaços em branco. | `'1 2 3'.split()` <br> `['1', '2', '3']` | Para separar números ou palavras que estão na mesma linha e são separados por espaços. |
| `map()` | Aplica uma função a cada item de um iterável (como uma lista) e retorna um objeto `map` (que pode ser convertido em lista). | `map(int, ['1', '2', '3'])` <br> `(produz ints 1, 2, 3)` | **Essencial na OBI** para converter rapidamente uma linha de strings (obtida de `.split()`) em uma lista de inteiros ou floats. |
| `list()` | Converte um iterável (como um objeto `map` ou uma tupla) em uma lista. | `list(map(int, ['1', '2']))` <br> `[1, 2]` | Usado junto com `map` para ter uma lista real que pode ser acessada por índices e percorrida múltiplas vezes. |
| `for ... in ...:` | Um loop que itera sobre os elementos de um iterável (lista, string, range, etc.). | `for fruta in ["maça", "banana"]:` | Para percorrer todos os elementos de uma lista, caracteres de uma string, ou executar um bloco de código um número fixo de vezes. |
| `range()` | Gera uma sequência de números. `range(n)` gera de 0 a `n-1`. `range(inicio, fim)` gera de `inicio` a `fim-1`. | `for i in range(5):` <br> `(i será 0, 1, 2, 3, 4)` | Muito usado para controlar loops `for` quando você precisa do índice ou quando sabe o número exato de repetições. |
| `_` (underscore) | Uma convenção em Python para uma variável "descartável" ou "não utilizada". | `for _ in range(N):` | Usado em loops quando você só precisa repetir `N` vezes e não se importa com o valor do contador do loop. |
| `append()` | Um método de lista que adiciona um item ao final da lista. | `minha_lista.append(item)` | Para construir listas dinamicamente, como adicionar linhas a uma matriz ou elementos a um vetor. |
| `print()` | Exibe um valor ou vários valores na saída padrão (tela), separados por espaços por padrão, e com uma nova linha no final. | `print("Olá", nome)` <br> `print(soma)` | Para mostrar os resultados do seu programa, conforme exigido pela saída do problema. |
| `if ... elif ... else:` | Estruturas condicionais que permitem ao programa tomar decisões. | `if idade >= 18: ...` <br> `elif idade > 12: ...` <br> `else: ...` | Essencial para implementar a lógica do problema, executando diferentes códigos dependendo de condições. |
| `while ...:` | Um loop que continua executando um bloco de código enquanto uma condição for verdadeira. | `while contador < 10: ...` | Usado quando o número de repetições não é fixo, mas depende de uma condição que muda durante a execução. |
| `len()` | Retorna o número de itens de um objeto (o tamanho de uma lista, o número de caracteres de uma string, etc.). | `tamanho = len(minha_lista)` | Para saber o tamanho de vetores ou strings, ou o número de linhas/colunas de uma matriz. |
| `[ ]` (colchetes) | Usado para criar listas ou para acessar elementos de listas (e strings). | `minha_lista = [1, 2, 3]` <br> `primeiro = minha_lista[0]` | Fundamental para trabalhar com vetores e matrizes. `matriz[linha][coluna]` |

-----

