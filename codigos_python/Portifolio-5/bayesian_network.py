import numpy as np  

P_SPAM = 0.4  # 40% dos e-mails são spam
P_NAO_SPAM = 1 - P_SPAM  # 60% não são spam

P_Gratis_Dado_SPAM = 0.8  # 80% dos e-mails de spam contêm "grátis"
P_Promocao_Dado_SPAM = 0.7  # 70% contêm "promoção"
P_Links_Dado_SPAM = 0.9  # 90% contêm links externo

P_Gratis_Dado_NAO_SPAM = 0.2  # 20% dos e-mails normais contêm "grátis"
P_Promocao_Dado_NAO_SPAM = 0.1  # 10% contêm "promoção"
P_Links_Dado_NAO_SPAM = 0.3  # 30% contêm links externos

# Calcula a probabilidade de um e-mail ser SPAM usando o Teorema de Bayes.
def calcular_probabilidade_spam(gratis, promocao, links):
    
    # Probabilidade conjunta de ser SPAM e conter certas palavras
    P_DADOS_DADO_SPAM = (
        (P_Gratis_Dado_SPAM if gratis else (1 - P_Gratis_Dado_SPAM)) *
        (P_Promocao_Dado_SPAM if promocao else (1 - P_Promocao_Dado_SPAM)) *
        (P_Links_Dado_SPAM if links else (1 - P_Links_Dado_SPAM))
    )
    
    # Probabilidade conjunta de NÃO ser SPAM e conter certas palavras
    P_DADOS_DADO_NAO_SPAM = (
        (P_Gratis_Dado_NAO_SPAM if gratis else (1 - P_Gratis_Dado_NAO_SPAM)) *
        (P_Promocao_Dado_NAO_SPAM if promocao else (1 - P_Promocao_Dado_NAO_SPAM)) *
        (P_Links_Dado_NAO_SPAM if links else (1 - P_Links_Dado_NAO_SPAM))
    )
    
    # Aplicando o Teorema de Bayes
    P_SPAM_DADO_DADOS = (P_DADOS_DADO_SPAM * P_SPAM) / (
        (P_DADOS_DADO_SPAM * P_SPAM) + (P_DADOS_DADO_NAO_SPAM * P_NAO_SPAM)
    )
    
    return P_SPAM_DADO_DADOS

# Teste do modelo: e-mail com "grátis", "promoção" e "links"
probabilidade = calcular_probabilidade_spam(gratis=1, promocao=0, links=1)
print(f"Probabilidade de ser SPAM: {probabilidade:.2%}")
