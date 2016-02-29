
import itertools
import operator
import math


import numpy


"""""
v = range(0, 20)
x = 0
vector = []
for e in itertools.combinations(v, 6):


    for t in range(len(e)):

        sal = e[t]

        if sal <= 15:

            s = sal

        print  sal
        """""
my_data1=[]
for run in range(1,31):

    train_x="./Results/Problem1/Res/test10_%d.txt"
    # C:\Users\Uriel\PycharmProjects\DeapTEST\Results\Problem1\Res\BestFitness_Out10_1.txt
    my_data1 = numpy.genfromtxt(train_x % run, delimiter=',', dtype=float)
    my_data.append(my_data1)
    matris=numpy.matris_[run,my_data1]

    #
print out