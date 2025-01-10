import random

professores = ["Algusto", "Maria", "Eduardo"]
materias = ["Matemática", "Física", "Química", "Biologia", "História"]
slots_tempo = [0, 1, 2, 3, 4]  # horários disponíveis

habilidades = {
    "Algusto": ["Matemática", "Física"],
    "Maria": ["Química", "Biologia"],
    "Eduardo": ["História", "Física"]
}

def criar_individuo():
    return [
        (random.choice(materias), random.choice(professores), random.choice(slots_tempo))
        for _ in range(len(materias))
    ]

def avaliar(individuo):
    conflitos = 0

    for materia, professor, _ in individuo:
        if materia not in habilidades[professor]:
            conflitos += 1

    # Verifica se há sobreposição de horários
    horarios_usados = [(slot, professor) for _, professor, slot in individuo]
    if len(horarios_usados) != len(set(horarios_usados)):
        conflitos += 1

    return -conflitos

# Função de cruzamento (crossover)
def cruzamento(pai1, pai2):
    ponto = random.randint(1, len(pai1) - 1)
    filho = pai1[:ponto] + pai2[ponto:]
    return filho

# Função de mutação
def mutacao(individuo):
    index = random.randint(0, len(individuo) - 1)
    materia, professor, slot = individuo[index]
    individuo[index] = (materia, random.choice(professores), random.choice(slots_tempo))

# Algoritmo Genético
def algoritmo_genetico(populacao_tamanho, geracoes, taxa_mutacao):
    # Criação da população inicial
    populacao = [criar_individuo() for _ in range(populacao_tamanho)]

    for geracao in range(geracoes):
        # Avaliação da população
        populacao = sorted(populacao, key=lambda ind: avaliar(ind), reverse=True)

        # Se a melhor solução não tiver conflitos para
        if avaliar(populacao[0]) == 0:
            break

        # Seleção
        nova_populacao = populacao[:2]

        # Cruzamento
        while len(nova_populacao) < populacao_tamanho:
            pai1 = random.choice(populacao[:10])  # Seleciona dos top 10
            pai2 = random.choice(populacao[:10])
            filho = cruzamento(pai1, pai2)
            nova_populacao.append(filho)

        # Mutação
        for individuo in nova_populacao[2:]:
            if random.random() < taxa_mutacao:
                mutacao(individuo)

        populacao = nova_populacao

    # Melhor solução encontrada
    melhor_solucao = populacao[0]
    return melhor_solucao, avaliar(melhor_solucao)

if __name__ == "__main__":
    # Parâmetros do AG
    populacao_tamanho = 50
    geracoes = 100
    taxa_mutacao = 0.1

    melhor_solucao, fitness = algoritmo_genetico(populacao_tamanho, geracoes, taxa_mutacao)

    print("Melhor solução encontrada:")
    for materia, professor, slot in melhor_solucao:
        print(f"Matéria: {materia}, Professor: {professor}, Horário: {slot}")
    print(f"\nFitness: {fitness}")
