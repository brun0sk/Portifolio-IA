import numpy as np

def prever_precos(preco_inicial, matriz_transicao, variacao, dias):
    estado_atual = 1
    precos = [preco_inicial]
    
    for _ in range(dias):
        estado_atual = np.random.choice([0, 1, 2], p=matriz_transicao[estado_atual])
        preco_atualizado = precos[-1] * (1 + variacao[estado_atual])
        precos.append(preco_atualizado)
    
    return precos

preco_inicial = 100
matriz_transicao = np.array([
    [0.7, 0.2, 0.1],
    [0.4, 0.5, 0.1],
    [0.2, 0.3, 0.5]
])
variacao = [0.02, 0, -0.02]
dias = 10

# Executar previsão
precos_previstos = prever_precos(preco_inicial, matriz_transicao, variacao, dias)

# Exibir resultados
print(precos_previstos)