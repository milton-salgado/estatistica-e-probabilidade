import numpy as np

num_casas = 20
num_iteracoes = 10000

def rolar_dados():
    return np.random.randint(1, 7, size=2)

def simular_ate_primeira_prisao():
    estado = (0, 0, 0)  # (posição, estágio, rodadas na prisão)
    passos = 0

    while True:
        posicao, estagio, prisao = estado
        dados = rolar_dados()
        passos += 1
        
        if prisao > 0:
            # Jogador está na prisão
            if dados[0] == dados[1]:
                # Solto se obtiver valores iguais
                prisao = 0
                estagio = 0
            else:
                # Continua preso
                prisao -= 1
            posicao = 10  # Fica na casa 10 enquanto está preso
        else:
            # Verificar se deve ir para a prisão
            if estagio == 2 and dados[0] == dados[1]:
                return passos  # Jogador vai para a prisão pela primeira vez
            else:
                # Atualizar posição no tabuleiro
                posicao = (posicao + sum(dados)) % num_casas
                
                # Verificar o estágio de suspeito
                if dados[0] == dados[1]:
                    estagio += 1
                else:
                    estagio = 0

        # Atualizar o estado
        estado = (posicao, estagio, prisao)

def realizar_experimentos(k):
    resultados = []
    for _ in range(k):
        passos_ate_primeira_prisao = simular_ate_primeira_prisao()
        resultados.append(passos_ate_primeira_prisao)
    return resultados

# Número de experimentos
k = 100000

# Realizar os experimentos
resultados_experimentos = realizar_experimentos(k)

# Exibir os resultados dos primeiros experimentos
print(resultados_experimentos[:10])
print(f"Média de passos até a primeira prisão: {np.mean(resultados_experimentos)}")
