import sys
from collections import deque

# --- Parte 1: Nossa Ferramenta BFS ---
# Esta função calcula a distância de um ponto de partida para todas as outras salas.
def bfs(ponto_de_partida, N, mapa):
    # Inicializa as distâncias como -1 (não visitado)
    distancias = [-1] * (N + 1)
    
    # Cria a fila e adiciona o ponto de partida
    fila = deque([ponto_de_partida])
    
    # A distância do ponto de partida para ele mesmo é 0
    distancias[ponto_de_partida] = 0
    
    # Loop principal do BFS
    while fila:
        sala_atual = fila.popleft()
        
        # Para cada vizinho da sala atual...
        for vizinho in mapa[sala_atual]:
            # Se o vizinho ainda não foi visitado...
            if distancias[vizinho] == -1:
                # Calcula a distância e adiciona na fila para visitar depois
                distancias[vizinho] = distancias[sala_atual] + 1
                fila.append(vizinho)
    
    # Retorna o array com todas as distâncias calculadas
    return distancias

# --- Lógica Principal ---

# 1. Leitura da Entrada (seu código)
N = int(sys.stdin.readline())
mapa = [[] for _ in range(N + 1)]

# O problema garante N >= 3, então não precisamos nos preocupar com N=1 ou N=2
for _ in range(N - 1):
    x, y = map(int, sys.stdin.readline().split())
    mapa[x].append(y)
    mapa[y].append(x)

# 2. Encontrar uma ponta do diâmetro (ponto_A)
# Começamos de um ponto arbitrário (sala 1) e achamos quem está mais longe.
dist_do_inicio = bfs(1, N, mapa)
maior_dist = -1
ponto_A = -1
for i in range(1, N + 1):
    if dist_do_inicio[i] > maior_dist:
        maior_dist = dist_do_inicio[i]
        ponto_A = i

# 3. Encontrar o diâmetro e a outra ponta (ponto_B)
# Agora, partindo do ponto_A, achamos a maior distância possível na árvore.
# Essa distância é o diâmetro.
dist_A = bfs(ponto_A, N, mapa)
diametro = -1
ponto_B = -1 # Precisamos de uma ponta B para a contagem
for i in range(1, N + 1):
    if dist_A[i] > diametro:
        diametro = dist_A[i]
        ponto_B = i

# --- Saída da Parte 1: Maior Ciclo ---
# O comprimento do ciclo é o diâmetro (número de túneis) + 1 (o túnel novo).
# Como o problema pede o número de salas, que já é D+1, a resposta é diametro + 1.
print(diametro + 1)


# --- Saída da Parte 2: Contagem de Maneiras ---
# Precisamos contar quantos nós estão em cada "ponta" dos diâmetros.

# Contagem de nós na ponta A: quantos nós estão à distância máxima do ponto_A?
contagem_A = 0
for i in range(1, N + 1):
    if dist_A[i] == diametro:
        contagem_A += 1

# Contagem de nós na ponta B: quantos nós estão à distância máxima do ponto_B?
dist_B = bfs(ponto_B, N, mapa)
contagem_B = 0
for i in range(1, N + 1):
    if dist_B[i] == diametro:
        contagem_B += 1
        
# O número de maneiras é a multiplicação das contagens de cada ponta.
print(contagem_A * contagem_B)