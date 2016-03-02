import itertools
import numpy as np
v = range(0, 20)
a=np.sum(v)
x = 0
vector = []
for e in itertools.combinations(v, 6):


    b=np.sum(e)
    b
    """"
    for t in range(len(e)):

        sal = e[t]

        #if sal <= 15:
    vector.append(e)
   # sumatoria=math.fsum(vector) / len(v)
   """""
    if a>b:
        a=b
print a





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
"""
Pro=1
Out=10
"""
for Pro in range(1,20):
    #for Out in range (10,100,10):
        #for run in range(1,31):

    train_x="./Results/Problem%d/train_x.txt"
    # C:\Users\Uriel\PycharmProjects\DeapTEST\Results\Problem1\Res\BestFitness_Out10_1.txt
    my_data1 = np.genfromtxt(train_x % Pro, delimiter=',')
    largo=len(my_data1)
    A.append(largo)# = numpy.vstack(A,my_data1)
    B.append(Pro)
     #   te=numpy.matrix(A)
    #B=te.mean(0)


np.sum([0.5, 1.5])
print A
print B