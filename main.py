from itertools import combinations

data = ['a1', 'c2', 'a2', 'b2', 'c1', 'd1', 'd2', 'b1']
pairs = combinations(data , 2)
games = combinations(pairs , int(len(data) / 2))

for game in games:
    if all(x[0] == y[0] for x , y in game):
        print(f"{game} - ikizler")
    else:
        print(f"{game} - ikizler eslesmedi")
