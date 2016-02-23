import math
from itertools import product
from fractions import gcd
from operator import itemgetter
import time

def hero(a,b,c):
    s = calcS(a,b,c)
    A = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return A

def calcS(a,b,c):
    return (a+b+c)/2.0

def isHeronian(a,b,c):
    a = hero(a,b,c)
    return a > 0 and a.is_integer()

def gcd3(x,y,z):
    return gcd(gcd(x,y),z)

def generateHeronianList(maxside):
    h = [(a,b,c,hero(a,b,c)) for a,b,c in product(range(1,maxside+1),repeat=3)
         if a <= b <= c and a+b > c and gcd3(a,b,c) == 1 and
         isHeronian(a,b,c)]
    return h

def printResults(heronianList,maxside):
    heronianList.sort(key=lambda x: (x[3], sum(x[:3]), x[:3])) #sort 
    print ('Number of Heronian triangles with sides up to %i: ' %maxside,len(heronianList))
    print ('\nFirst ten ordered by increasing area, then perimeter, then side length:')
    print ('\n'.join(' %14r perim: %3i area: %i'%(sides[:3],sum(sides[:3]),sides[3]) for sides in heronianList[:10]))
    return

def generateTriangles(maxside):
    h = [(a,b,c) for a,b,c in product(range(1,maxside+1),repeat=3)
         if a <= b <= c and a+b > c and gcd3(a,b,c) == 1 and
         isHeronian(a,b,c)]

    h.sort(key = lambda x: (hero(*x), sum(x), x[::-1]))   # By increasing area, perimeter, then sides

    print('Primitive Heronian triangles with sides up to %i:' % maxside, len(h))
    print('\nFirst ten when ordered by increasing area, then perimeter,then maximum sides:')
    print('\n'.join('  %14r perim: %3i area: %i' 
                    % (sides, sum(sides), hero(*sides)) for sides in h[:10]))
##    print('\nAll with area 210 subject to the previous ordering:')
##    print('\n'.join('  %14r perim: %3i area: %i' 
##                    % (sides, sum(sides), hero(*sides)) for sides in h
##                    if hero(*sides) == 210))

def compareRuntime():
    number_of_trials = 10

    #Generate Triangles
    gt_results = []
    for i in range(number_of_trials):
        startTime = time.time()
        generateTriangles(200)
        endTime = time.time()
        gt_results.append(endTime-startTime)
    #Print Results
    pr_results = []
    for i in range(number_of_trials):
        startTime = time.time()
        printResults(generateHeronianList(200),200)
        endTime = time.time()
        pr_results.append(endTime-startTime)

    print 'GT results: {}sec'.format(sum(gt_results)/len(gt_results))
    print 'PR results: {}sec'.format(sum(pr_results)/len(pr_results))

def main():
    maxsides = 200
    printResults(generateHeronianList(maxsides),maxsides)
