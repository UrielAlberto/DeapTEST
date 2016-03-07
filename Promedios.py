import numpy
import itertools



for Funcion in range (1,4):
    for problema in range(1,12):
        for cont in range(10, 100, 10):
            for run in range(1,31):
                Best="./Results/Problem%d/Res%d/BestOut%d_%d.txt"
                AvgSize="./Results/Problem%d/Res%d/BestSizeAvge%d_%d.txt"
                BestSize="./Results/Problem%d/Res%d/BestSize%d_%d.txt"
                my_data1 = numpy.genfromtxt(Best % (problema, Funcion, cont,run), delimiter=' ', dtype=float)
                my_data2 = numpy.genfromtxt(AvgSize % (problema, Funcion, cont,run), delimiter=' ', dtype=float)
                my_data3 = numpy.genfromtxt(BestSize % (problema, Funcion, cont,run), delimiter=' ', dtype=float)


                A=[]
                B=[]
                """
                Out=10
                Problema=1
                for Run in range(1,11):
                    vector="./Results/Problem%d/Res/BestOut%d_%d.txt"
                    # C:\Users\Uriel\PycharmProjects\DeapTEST\Results\Problem1\Res\BestFitness_Out10_1.txt
                    matri = numpy.genfromtxt(vector % (Problema,Out,Run), delimiter=',', dtype=float)

                A.insert(Run,matri)# = numpy.vstack(A,my_data1)
                te=numpy.matrix(A)
            B=te.mean(0)

            fig =plt.figure(1)
            plt.subplot(221)
            plt.plot(points,points5,'go')

            plt.subplot(222)
            plt.plot(points,points2,'bo')

            plt.subplot(223)
            plt.plot(points3,B,'rs')
            fig.savefig('./Results/Problem%d/Res/best%d.eps'%(problema,Out), dpi=fig.dpi)
            plt.close(fig)
                            """""