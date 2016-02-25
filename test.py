import itertools

v = range(0, 20)
x = 0
vector = []
for e in itertools.combinations(v, 6):


    for t in range(len(e)):

        sal = e[t]

        if sal <= 15:

            s = sal

        print  sal
