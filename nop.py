program = input()
inst_loc = []
for i, c in enumerate(program):
    if c.isupper():
        inst_loc.append(i)
adds = 0
for i in range(len(inst_loc)):
    #print(inst_loc)
    add = (4 - (inst_loc[i] % 4)) % 4
    for j in range(i, len(inst_loc)):
        inst_loc[j] += add
    adds += add
print(adds)
