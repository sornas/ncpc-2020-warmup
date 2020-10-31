opts = "SPR"
beats = { "S": "P", "P": "R", "R": "S" }

"""
The first line contains the integer R (1≤R≤50), the number of
rounds played.
"""
rounds = int(input())
"""
The second line contains a string of R letters ‘S’, ‘P’ or
‘R’. The string represents symbols that Sven showed in each round. ‘S’
is for scissors, ‘P’ for paper, ‘R’ for rock.
"""
sven = input()

"""
The third line contains the integer N (1≤N≤50), the number of friends.
"""
n = int(input())

"""
Each of the following N lines contains a string of R letters ‘S’, ‘P’
or ‘R’. These are the symbols shown by each of the N friends in each
of the R rounds.
"""
friends = [[0, 0, 0] for _ in range(rounds)]  # chosen S P R per round
for _ in range(n):
    friend_total = input()
    for i, friend_in_round in enumerate(friend_total):
        if friend_in_round == "S":
            friends[i][0] += 1
        elif friend_in_round == "P":
            friends[i][1] += 1
        elif friend_in_round == "R":
            friends[i][2] += 1

"""
Output Sven’s actual score on the first line.
"""
points = 0
for i in range(rounds):
    points += friends[i][opts.index(sven[i])] + friends[i][opts.index(beats[sven[i]])] * 2
print(points)

"""
Output his largest possible score on the second line, assuming his
friends didn’t change their symbols.
"""
max_points = []
for i in range(rounds):
    best = 0
    for idx, opt in enumerate(opts):
        cand = friends[i][idx] * 1 + friends[i][opts.index(beats[opt])] * 2
        if cand > best:
            best = cand
    max_points.append(best)
print(sum(max_points))
