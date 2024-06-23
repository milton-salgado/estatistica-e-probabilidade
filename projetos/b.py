import numpy as np

# Inicializando a matriz 60x60 com zeros
P = np.zeros((60, 60))

# Probabilidades ajustadas das somas de dois dados diferentes
probabilidades_diferentes = {
    3: 2/36,
    4: 2/36,
    5: 4/36,
    6: 4/36,
    7: 6/36,
    8: 4/36,
    9: 4/36,
    10: 2/36,
    11: 2/36
}

# Função para determinar a próxima casa após rolar dois dados
def next_house(i, roll):
    return (i + roll) % 20

# Primeiras 20 linhas (estados 0 a 19)
for i in range(20):
    # Transições baseadas em dados diferentes
    for roll, prob in probabilidades_diferentes.items():
        P[i, next_house(i, roll)] += prob
    # Transição para o estágio 1 de suspeito
    P[i, i + 20] = 1/6

# Segundas 20 linhas (estados 20 a 39)
for i in range(20, 40):
    house = i - 20
    # Transições baseadas em dados diferentes
    for roll, prob in probabilidades_diferentes.items():
        P[i, next_house(house, roll)] += prob
    # Transição para o estágio 2 de suspeito
    P[i, i + 20] = 1/6

# Terceiras 20 linhas (estados 40 a 59)
for i in range(40, 60):
    house = i - 40
    # Transições baseadas em dados diferentes
    for roll, prob in probabilidades_diferentes.items():
        P[i, next_house(house, roll)] += prob
    P[i, 29] = 1/6

# Resolver o sistema πP = π
valores, vetores = np.linalg.eig(P.T)
vetor_estacionario = np.real(vetores[:, np.isclose(valores, 1)])
vetor_estacionario = vetor_estacionario / vetor_estacionario.sum()
vetor_estacionario = vetor_estacionario[:, 0]

# Distribuição estacionária para as 20 casas
distribuicao_estacionaria = vetor_estacionario[:20] + vetor_estacionario[20:40] + vetor_estacionario[40:60]

# Casa onde o jogador passa mais tempo
casa_mais_tempo = np.argmax(distribuicao_estacionaria)
tempo_medio = distribuicao_estacionaria[casa_mais_tempo]

print(f"Distribuição estacionária: {distribuicao_estacionaria}")
print(f"Casa onde o jogador passa mais tempo: {casa_mais_tempo} com probabilidade {tempo_medio:.4f}")
