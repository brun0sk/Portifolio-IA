import numpy as np

class FiltroKalman:
    def __init__(self, F, B, H, Q, R, x0, P0):
        self.F = F  # Modelo de transição de estado
        self.B = B  # Modelo de controle
        self.H = H  # Matriz de observação
        self.Q = Q  # Covariância do ruído do processo
        self.R = R  # Covariância do ruído da medição
        self.x = x0  # Estado inicial
        self.P = P0  # Matriz de covariância inicial
    
    def prever(self, u):
        # Prever o estado e a covariância do estado
        self.x = np.dot(self.F, self.x) + np.dot(self.B, u)
        self.P = np.dot(np.dot(self.F, self.P), self.F.T) + self.Q
        return self.x
    
    def atualizar(self, z):
        # Calcular o ganho de Kalman
        S = np.dot(np.dot(self.H, self.P), self.H.T) + self.R
        K = np.dot(np.dot(self.P, self.H.T), np.linalg.inv(S))
        
        # Atualizar a estimativa do estado e a matriz de covariância
        y = z - np.dot(self.H, self.x)  # Erro de inovação
        self.x = self.x + np.dot(K, y)
        I = np.eye(self.P.shape[0])
        self.P = np.dot(np.dot(I - np.dot(K, self.H), self.P), (I - np.dot(K, self.H)).T) + np.dot(np.dot(K, self.R), K.T)
        
        return self.x

# Definição das matrizes do filtro de Kalman
F = np.array([[1, 1], [0, 1]])  # Modelo de transição de estado
B = np.array([[0.5], [1]])      # Modelo de controle
H = np.array([[1, 0]])          # Matriz de observação
Q = np.array([[1, 0], [0, 1]])  # Covariância do ruído do processo
R = np.array([[1]])             # Covariância do ruído da medição

# Estado inicial e matriz de covariância inicial
estado_inicial = np.array([[0], [1]])
P0 = np.array([[1, 0], [0, 1]])

# Criar instância do Filtro de Kalman
filtro_kalman = FiltroKalman(F, B, H, Q, R, estado_inicial, P0)

# Prever e atualizar com entrada de controle e medições do GPS
entrada_controle = np.array([[1]])  # Aceleração do carro
medicao_gps = np.array([[1]])  # Posição medida pelo GPS

# Etapa de previsão
estado_previsto = filtro_kalman.prever(entrada_controle)
print("Estado previsto:\n", estado_previsto)

# Etapa de atualização
estado_atualizado = filtro_kalman.atualizar(medicao_gps)
print("Estado atualizado:\n", estado_atualizado)
