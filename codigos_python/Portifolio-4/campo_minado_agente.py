import random
import numpy as np

# Representação do Tabuleiro
def criar_tabuleiro(tamanho, num_minas):
    tabuleiro = np.zeros((tamanho, tamanho), dtype=int)

    # Coloca minas aleatoriamente
    minas_colocadas = 0
    while minas_colocadas < num_minas:
        x, y = random.randint(0, tamanho - 1), random.randint(0, tamanho - 1)
        if tabuleiro[x][y] == 0:
            tabuleiro[x][y] = -1  # Representa uma mina
            minas_colocadas += 1

    # Calcula os números adjacentes a cada célula
    for x in range(tamanho):
        for y in range(tamanho):
            if tabuleiro[x][y] == -1:
                continue
            tabuleiro[x][y] = contar_minas_adjacentes(tabuleiro, x, y)

    return tabuleiro

def contar_minas_adjacentes(tabuleiro, x, y):
    # Conta o número de minas adjacentes a uma célula.
    minas = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < tamanho and 0 <= ny < tamanho and tabuleiro[nx][ny] == -1:
                minas += 1
    return minas

def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(str(c) if c != -1 else "B" for c in linha))

# Base de Conhecimento (KB)
def obter_celulas_adjacentes(tabuleiro, x, y):
    """Obtém as células adjacentes a uma posição."""
    adjacentes = []
    tamanho = len(tabuleiro)
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < tamanho and 0 <= ny < tamanho:
                adjacentes.append((nx, ny))
    return adjacentes

def aplicar_regras(tabuleiro_conhecido, tabuleiro_real):
    # Aplica regras dedutivas para marcar células seguras ou minas
    novas_revelacoes = []

    for x in range(len(tabuleiro_conhecido)):
        for y in range(len(tabuleiro_conhecido)):
            if tabuleiro_conhecido[x][y].isdigit():
                valor = int(tabuleiro_conhecido[x][y])
                adjacentes = obter_celulas_adjacentes(tabuleiro_conhecido, x, y)
                desconhecidas = [(nx, ny) for nx, ny in adjacentes if tabuleiro_conhecido[nx][ny] == '?']
                minas = [(nx, ny) for nx, ny in adjacentes if tabuleiro_conhecido[nx][ny] == 'B']

                # Regra 1: Todas as células desconhecidas são minas
                if len(desconhecidas) == valor - len(minas):
                    for nx, ny in desconhecidas:
                        tabuleiro_conhecido[nx][ny] = 'B'

                # Regra 2: Todas as células desconhecidas são seguras
                if len(minas) == valor:
                    for nx, ny in desconhecidas:
                        if tabuleiro_conhecido[nx][ny] == '?':
                            tabuleiro_conhecido[nx][ny] = str(tabuleiro_real[nx][ny])
                            novas_revelacoes.append((nx, ny))

    return novas_revelacoes

def agente_campo_minado(tabuleiro_real):
    tamanho = len(tabuleiro_real)
    tabuleiro_conhecido = np.full((tamanho, tamanho), '?', dtype=str)

    # Jogada inicial
    x, y = random.randint(0, tamanho - 1), random.randint(0, tamanho - 1)
    if tabuleiro_real[x][y] == -1:
        print("O agente perdeu na primeira jogada!")
        return

    tabuleiro_conhecido[x][y] = str(tabuleiro_real[x][y])

    # Ciclo do agente
    while '?' in tabuleiro_conhecido:
        novas_revelacoes = aplicar_regras(tabuleiro_conhecido, tabuleiro_real)

        # Se nenhuma nova célula for revelada, escolha aleatoriamente
        if not novas_revelacoes:
            x, y = random.randint(0, tamanho - 1), random.randint(0, tamanho - 1)
            while tabuleiro_conhecido[x][y] != '?':
                x, y = random.randint(0, tamanho - 1), random.randint(0, tamanho - 1)

            if tabuleiro_real[x][y] == -1:
                print("O agente perdeu!")
                return

            tabuleiro_conhecido[x][y] = str(tabuleiro_real[x][y])

        print("Tabuleiro conhecido pelo agente:")
        exibir_tabuleiro(tabuleiro_conhecido)

    print("O agente venceu! Tabuleiro final conhecido:")
    exibir_tabuleiro(tabuleiro_conhecido)

if __name__ == "__main__":
    while True:
        dificuldade = int(input("Insira dificuldade: \n 1- Fácil \n 2- Media \n 3-Dificil \n"))

        if (dificuldade == 1):
            tamanho = 9
            num_minas = 10
            break
        elif (dificuldade == 2):
            tamanho = 16
            num_minas = 40
            break
        elif (dificuldade == 3):
            tamanho = 24
            num_minas = 99
            break
        else:
            print("Valor inválido\n")

    
    tabuleiro_real = criar_tabuleiro(tamanho, num_minas)
    print("Tabuleiro real (oculto para o agente):")
    exibir_tabuleiro(tabuleiro_real)

    agente_campo_minado(tabuleiro_real)