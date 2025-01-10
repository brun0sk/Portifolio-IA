import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
    print()

def is_winner(board, player):
    "Verifica se o jogador atual venceu."
    # Linhas
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Colunas
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    # Diagonais
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    "Verifica se o tabuleiro está cheio (empate)"
    return all(cell != " " for row in board for cell in row)

def get_available_moves(board):
    """Retorna as posições disponíveis no tabuleiro."""
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def alpha_beta_pruning(board, depth, alpha, beta, maximizing_player):

    # Verifica condições de vitória ou empate
    if is_winner(board, "X"):
        return 10 - depth, None
    if is_winner(board, "O"):
        return depth - 10, None
    if is_full(board):
        return 0, None

    if maximizing_player:  # Jogador "X"
        max_eval = -math.inf
        best_move = None
        for (r, c) in get_available_moves(board):
            board[r][c] = "X"
            eval, _ = alpha_beta_pruning(board, depth + 1, alpha, beta, False)
            board[r][c] = " "
            if eval > max_eval:
                max_eval = eval
                best_move = (r, c)
            alpha = max(alpha, eval)
            if beta <= alpha:  # Corte beta
                break
        return max_eval, best_move
    else:  # Jogador "O"
        min_eval = math.inf
        best_move = None
        for (r, c) in get_available_moves(board):
            board[r][c] = "O"
            eval, _ = alpha_beta_pruning(board, depth + 1, alpha, beta, True)
            board[r][c] = " "
            if eval < min_eval:
                min_eval = eval
                best_move = (r, c)
            beta = min(beta, eval)
            if beta <= alpha:  # Corte alfa
                break
        return min_eval, best_move

if __name__ == "__main__":
    # Tabuleiro inicial
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Jogo da Velha - Alpha-Beta Pruning\n")
    print_board(board)

    while True:
        # Jogador "X" (IA)
        _, move = alpha_beta_pruning(board, 0, -math.inf, math.inf, True)
        if move:
            board[move[0]][move[1]] = "X"
        print("Jogador X (IA) jogou:")
        print_board(board)
        if is_winner(board, "X"):
            print("Jogador X venceu!")
            break
        if is_full(board):
            print("Empate!")
            break

        # Jogador "O" (Humano)
        print("Jogador O, sua vez! (Digite linha e coluna de 0 a 2 separados por espaço)")
        while True:
            try:
                r, c = map(int, input("Linha e Coluna: ").split())
                if board[r][c] == " ":
                    board[r][c] = "O"
                    break
                else:
                    print("Essa posição já está ocupada!")
            except (ValueError, IndexError):
                print("Entrada inválida. Tente novamente!")
        print_board(board)
        if is_winner(board, "O"):
            print("Jogador O venceu!")
            break
        if is_full(board):
            print("Empate!")
            break
