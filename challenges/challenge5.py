def pick_bball_game(p):
    """
    prob_game1 = p
    prob_game2 = P(make 1+2) + P(make 1+3) + P(make 2+3) + P(make 1+2+3)
    prob_game2 = p*p*(1-p) + p*(1-p)*p + (1-p)*p*p + p*p*p
    prob_game2 = p**2 - p**3 + p**2 - p**3 + p**2 - p**3 + p**3
    prob_game2 = 3 * p ** 2 - 2 * p ** 3
    prob_game1 > prob_game2
    p > 3 * p ** 2 - 2 * p ** 3
    1 > 3 * p - 2 * p ** 2
    2 * p ** 2 - 3 * p + 1 > 0
    (p - 1) * (2 * p - 1) > 0
    p < 1, both terms must be negative
    (2 * p - 1) < 0
    p < 0.5
    """
    if p == 0 or p == 1 or p == 0.5:
        return 0
    elif p < 0.5:
        return 1
    else:
        return 2
