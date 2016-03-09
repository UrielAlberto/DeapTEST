import numpy
import itertools

import matplotlib.pyplot as plt



for problema in range(1,12):
    for cont in range(10, 100, 10):
        A=[]
        B=[]
        test_x="./Results/Problem%d/test_x.txt"
        my_data3 = numpy.genfromtxt(test_x % problema, delimiter=' ')
        for run in range(1,31):
            Best="./Results/Problem%d/Res/BestOut%d_%d.txt"
          #  AvgSize="./Results/Problem%d/Res/BestSizeAvge%d_%d.txt"
          #  BestSize="./Results/Problem%d/Res/BestSize%d_%d.txt"
            my_data1 = numpy.genfromtxt(Best % (problema, cont,run), delimiter=' ', dtype=float)
          #  my_data2 = numpy.genfromtxt(AvgSize % (problema, cont,run), delimiter=' ', dtype=float)
          #  my_data3 = numpy.genfromtxt(BestSize % (problema, cont,run), delimiter=' ', dtype=float)




            A.insert(run,my_data1)# = numpy.vstack(A,my_data1)
            te=numpy.matrix(A)
        B=te.mean(0)
        outfile = open('./Results/Problem%d/test%d.txt'%(problema,cont),'ab')


        out=numpy.array(B,dtype=float)
        numpy.savetxt(outfile, out, delimiter=' ')
        Best="./Results/Problem%d/test%d.txt"
        my_data2 = numpy.genfromtxt(Best % (problema, cont), delimiter=' ', dtype=float)


        fig =plt.figure(1)
        plt.subplot(221)
        plt.plot(my_data3,my_data2,'go')

        plt.subplot(222)
        plt.plot(my_data3,my_data2,'bo')

        plt.subplot(223)
        plt.plot(my_data3,my_data2,'rs')
        plt.close(fig)