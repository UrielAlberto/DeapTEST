# print("Hello putito")
# print("Hello 2 putito")
# print 'hello tito'
#    This file is part of EAP.
#
#    EAP is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of
#    the License, or (at your option) any later version.
#
#    EAP is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with EAP. If not, see <http://www.gnu.org/licenses/>.
import itertools
import operator
import math
import random
import matplotlib.pyplot as plt

import numpy

from deap import algorithms
from deap import base
from deap import creator
from deap import tools
from deap import gp

# Define new functions
def protectedDiv(left, right):
    with numpy.errstate(divide='ignore',invalid='ignore'):
        x = numpy.divide(left, right)
        if isinstance(x, numpy.ndarray):
            x[numpy.isinf(x)] = 1
            x[numpy.isnan(x)] = 1
        elif numpy.isinf(x) or numpy.isnan(x):
            x = 1
    return x

pset = gp.PrimitiveSet("MAIN", 1)
pset.addPrimitive(operator.add, 2)
pset.addPrimitive(operator.sub, 2)
pset.addPrimitive(operator.mul, 2)
pset.addPrimitive(protectedDiv, 2)
pset.addPrimitive(operator.neg, 1)
pset.addPrimitive(math.cos, 1)
pset.addPrimitive(math.sin, 1)
pset.addEphemeralConstant("rand101", lambda: random.randint(-1,1))
pset.renameArguments(ARG0='x')

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
# creator.create("FitnessMinTest", base.Fitness, weights=(-1.0,))

creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=2)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("compile", gp.compile, pset=pset)

def evalSymbReg(individual, points,points2, funcion,cont):
    # Transform the tree expression in a callable function
    func = toolbox.compile(expr=individual)
    #S=func

    # Evaluate the mean squared error between the expression
    # and the real function : x**4 + x**3 + x**2 + x

    # print individual
    # import matplotlib.pyplot as plt
    # plt.plot(func,points2)
    # plt.ylabel('some numbers')
    # plt.show()
    # sqerrors2 = (func(points[x]) for x in range(len(points)))

    if funcion==1:#Funcion normal
        Sqerrors = ((func(points[x]) - points2[x])**2 for x in range(len(points)))
        sqerrors=math.fsum(Sqerrors) / len(points)
    if funcion==2:#Funcion objetivo LMS
        Cont=20
        ind=0
        sal=[]
        Largo=len(points)
        outlayer=Largo*(float(Cont / 100.0))
        porciento=int(Largo-outlayer)
        if float(Cont/100.0)>0.5:
            porciento=int(Largo-Largo*(float(0.5)))
        for t in range(len(points)):
            temp=t
            salida = ((func(points[temp]) - points2[temp])**2 )
            sal.insert(ind,salida)
            ind=ind+1
        sqerrors=numpy.median(sal)
        for e in itertools.combinations(sal, porciento):
            OutVec2=numpy.median(e)#LSM MAGIC
            if sqerrors >= OutVec2:
                sqerrors = OutVec2
    if funcion==3:#Funcion objetivo LTS
        Cont=20
        ind=0
        sal=[]
        Largo=len(points)
        outlayer=Largo*(float(Cont / 100.0))
        porciento=int(Largo-outlayer)
        if float(Cont/100.0)>0.5:
            porciento=int(Largo-Largo*(float(0.5)))
        for t in range(len(points)):
            temp=t
            salida = ((func(points[temp]) - points2[temp])**2 )
            sal.insert(ind,salida)
            ind=ind+1
        sqerrors=numpy.sum(sal)/porciento
        for e in itertools.combinations(sal, porciento):
            OutVec2=numpy.sum(e)/porciento #LTS MAGIC
            if sqerrors >= OutVec2:
                sqerrors = OutVec2
    return sqerrors,


    return sqerrors,
def evalSymbRegBest(individual, points,points2,points3,points5,run,Funcion):
    # Transform the tree expression in a callable function
    func = toolbox.compile(expr=individual)

   # print individual
    sqerrors2=[]
    for x in range(len(points3)):
        sqerrors2.append(func(points3[x]))
    print len
    #---Aqui generamos y los pinches arrays numpy a txt para despues promediarlo
    outfile = open('./Results/Problem%d/Res%d/BestOut%d_%d.txt'%(problema,Funcion,cont,run),'ab')

    #outfile.write("%s "%sqerrors2)
    #outfile = open('./Problem%s/Res/test_Out%s_%s.txt'%(problema,cont,run, 'a'))
    out=numpy.array(sqerrors2,dtype=float)
    numpy.savetxt(outfile, out, delimiter='')
    #-----------------Experimento perron :v
    """
    if run==10:
        A=[]
        B=[]
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


    """ #exprimento perron fin sad*



def Test(train_x,train_y,Funcion,cont):
    # direccion1=trainx
    # direccion2="./Problem1/test_x.txt"

    my_data1 = train_x
    my_data2 = train_y

    toolbox.register("evaluate", evalSymbReg, points=my_data1, points2=my_data2, funcion=Funcion,cont=cont)
    # toolbox.register("evaluate", evalSymbReg, points=my_data2)


toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", gp.cxOnePoint)
toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)

toolbox.decorate("mate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))
toolbox.decorate("mutate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))

def main(problema,cont,run,Funcion):
    #random.seed(318)
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

            Test(my_data1,my_data2,Funcion,cont)

            pop = toolbox.population(n=100)
            hof = tools.HallOfFame(3)

            stats_fit = tools.Statistics(lambda ind: ind.fitness.values)
            stats_size = tools.Statistics(len)
            mstats = tools.MultiStatistics(fitness=stats_fit, size=stats_size)
            mstats.register("avg", numpy.mean)
            mstats.register("std", numpy.std)
            mstats.register("min", numpy.min)
            mstats.register("max", numpy.max)

            pop, log, avg_size = algorithms.eaSimple(pop, toolbox, 0.9, 0.1, 200, problema,cont,run,Funcion,stats=mstats,
                                       halloffame=hof, verbose=True)
            # print log
            # logging.info("Best individual is %s, %s", gp.evaluate(hof[0]), hof[0].fitness)
            # hof[0]
            var=evalSymbRegBest(hof[0],my_data1,my_data2,my_data3,my_data5,run,Funcion)
            outfile2 = open('./Results/Problem%d/Res%d/BestSize%d_%d.txt'%(problema,Funcion,cont,run),'ab')
            outfile2.write('\n%s;%s'%(len(hof[0]),avg_size))


            """ Descomentar esto si quieres el mejor invidivuo
            outfile = open('./Results/Problem%d/BestFitness_%d.txt'%(problema,cont), 'a')
            outfile.write("\n%s"%hof[0])
            """
            # outfile = open('popfinal.txt', 'w')

            # outfile.write("\n Best individual is: %s  %s" %( hof[0].fitness,  str(hof[0])))
            # outfile.write("\n Best individual is: %s %s" % ( hof[1].fitness, str(hof[1])))
            # outfile.write("\n Best individual is: %s %s " % ( hof[2].fitness,  str(hof[2])))
            # Var=[]
            # Var.insert(runs,var[0])
            # list((Var))


            return pop, log, hof



if __name__ == "__main__":
    Funcion=3


    for problema in range(1,12):
        for cont in range(10, 100, 10):
            for run in range(1,31):
                main(problema, cont, run, Funcion)


    """""
    problema=1

    cont=10
    Funcion=1

    for run in range(1,11):

        main(problema, cont, run,Funcion)
    #main(problema, cont)
     """
    print Var[:]