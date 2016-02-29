
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
A=[]
B=[]
for run in range(1,11):

    train_x="./Results/Problem1/Res/test10_%d.txt"
    # C:\Users\Uriel\PycharmProjects\DeapTEST\Results\Problem1\Res\BestFitness_Out10_1.txt
    my_data1 = numpy.genfromtxt(train_x % run, delimiter=',', dtype=float)

    A.insert(run,my_data1)# = numpy.vstack(A,my_data1)
    te=numpy.matrix(A)
B=te.mean(0)
k= 51
print B