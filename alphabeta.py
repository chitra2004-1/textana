def alpha_beta(values, depth, index, alpha, beta, maximizing_player):
    if depth == 0 or index >= len(values):
        if index < len(values):
            return values[index]
        else:
            return 0
    if maximizing_player:
        max_eval = float('-inf')
        for i in range(2):
            eval = alpha_beta(values, depth - 1, index * 2 + i, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha: break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(2):
            eval = alpha_beta(values, depth - 1, index * 2 + i, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha: break
        return min_eval
values = [3, 5, 2, 9, 12, 7, 10, 14]
print("Optimal value:", alpha_beta(values, 3, 0, float('-inf'), float('inf'), True))
