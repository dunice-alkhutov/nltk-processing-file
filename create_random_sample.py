import random

rnd_lines = []
while len(rnd_lines) < 100:
    rnd = random.randint(1, 612000)
    if rnd not in rnd_lines:
        rnd_lines.append(rnd)

dst = open('dst.txt', 'w')

with open("dump 2.txt") as fp:
    for i, line in enumerate(fp):
        if i in rnd_lines:
            dst.write(line)
dst.close