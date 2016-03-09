import numpy
import itertools

import matplotlib.pyplot as plt



for problema in range(1,12):
    for cont in range(10, 100, 10):
        A=[]
        B=[]

        train_x="./Results/Problem%d/train_x.txt"
        train_y="./Results/Problem%d/OutLy%d.txt"
        test_x="./Results/Problem%d/test_x.txt"
        test_y="./Results/Problem%d/test_y.txt"
        trainp_y="./Results/Problem%d/train_y.txt"
        my_data1 = numpy.genfromtxt(train_x % problema, delimiter=' ')
        my_data2 = numpy.genfromtxt(train_y % (problema,  cont), delimiter=' ')
        my_data3 = numpy.genfromtxt(test_x % problema, delimiter=' ')
        my_data4 = numpy.genfromtxt(test_y % problema, delimiter=' ')
        my_data5 = numpy.genfromtxt(trainp_y % problema, delimiter=' ')
        """
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
        """
        Best="./Results/Problem%d/BestProm%d.txt"
        my_data6 = numpy.genfromtxt(Best % (problema, cont), delimiter=' ', dtype=float)


        fig =plt.figure(1)
        plt.subplot(221)
        plt.plot(my_data1,my_data5,'go')

        plt.subplot(222)
        plt.plot(my_data1,my_data2,'bo')

        plt.subplot(223)
        plt.plot(my_data3,my_data6,'rs')
        plt.close(fig)
        fig.savefig('./Results/Problem%d/BestProm%d.eps'%(problema,cont), dpi=fig.dpi)
        plt.close(fig)
