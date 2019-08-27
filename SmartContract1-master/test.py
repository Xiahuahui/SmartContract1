import nashpy as nash
A = [[1, 2], [3, 0]]
B = [[0, 2], [3, 1]]
game = nash.Game(A, B)
for eq in game.support_enumeration():
    print(eq)