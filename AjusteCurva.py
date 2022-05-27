from ast import Return
from audioop import reverse
from cmath import cos, sin
from inspect import ClosureVars
import math
from pickle import TRUE
import numpy as np
from matplotlib import pyplot as plt
import random
import pandas as pd


def Inicialgraficas():
    graficas = []
    for i in range(0,100):
        A1= random.randrange(1,255, 1)
        B1=random.randrange(1,255, 1)
        C1=random.randrange(1,255, 1)
        D1=random.randrange(1,255, 1)
        E1=random.randrange(1,255, 1)
        F1=random.randrange(1,255, 1)
        G1=random.randrange(1,255, 1) 
        graficas.append([A1, B1, C1, D1, E1, F1,G1])
    
    return graficas


# Graficas 
def graficar(Graficas,iteracion):
    Peso=5  
    A=8
    B=25
    C=4
    D=45
    E=10
    F=17
    G=35
    A2=Graficas[iteracion][0]/Peso
    B2=Graficas[iteracion][1]/Peso
    C2=Graficas[iteracion][2]/Peso
    D2=Graficas[iteracion][3]/Peso
    E2=Graficas[iteracion][4]/Peso
    F2=Graficas[iteracion][5]/Peso
    G2=Graficas[iteracion][6]/Peso
    x=[]
    y=[]
    x_2=[]
    y_2=[]
    FA=[]
    aptitud = 0
    i=0
    while(i <= 1000):
      x.append((i+1)/10);
      y.append(A*(B*sin(x[i]/C)+D*cos(x[i]/E))+F*x[i]-G)
      x_2.append((i+1)/10);
      y_2.append(A2* (B2*sin(x_2[i]/C2)+D2*cos(x_2[i]/E2))+F2*x_2[i]-G2)
      FA.append(abs(y[i]-y_2[i]))
      i=i+1
   
    
    for valor in FA:
        aptitud = aptitud + valor
    d1 = {
        "cromosomas": [Graficas[iteracion][0],Graficas[iteracion][1], Graficas[iteracion][2], Graficas[iteracion][3], Graficas[iteracion][4],Graficas[iteracion][5],Graficas[iteracion][6]],
        "Error": aptitud
    }
    return d1

def graficarfinal(GraficasFinal):
    contador=0
    A=8
    B=25
    C=4
    D=45
    E=10
    F=17
    G=35
    Peso=5
    A2=GraficasFinal[0]["cromosomas"][0]/Peso
    B2=GraficasFinal[0]["cromosomas"][1]/Peso
    C2=GraficasFinal[0]["cromosomas"][2]/Peso
    D2=GraficasFinal[0]["cromosomas"][3]/Peso
    E2=GraficasFinal[0]["cromosomas"][4]/Peso
    F2=GraficasFinal[0]["cromosomas"][5]/Peso
    G2=GraficasFinal[0]["cromosomas"][6]/Peso
    
    x=[]
    y=[]
    x_2=[]
    y_2=[]
    FA=[]
    aptitud = 0
    i=0
    while(i <= 1000):
      x.append((i+1)/10);
      y.append(A*(B*sin(x[i]/C)+D*cos(x[i]/E))+F*x[i]-G)
      x_2.append((i+1)/10);
      y_2.append(A2* (B2*sin(x_2[i]/C2)+D2*cos(x_2[i]/E2))+F2*x_2[i]-G2)
      FA.append(abs(y[i]-y_2[i]))
      i=i+1
   
    plt.figure(1)
    plt.plot(x,y)
    plt.plot(x_2,y_2)
    plt.title("Historial de ajuste de curva")
    plt.show(block=False)
  
    plt.pause(0.5)
    plt.clf()
    
    for valor in FA:
        aptitud = aptitud + valor
    
    d1 = {
        "cromosomas": [GraficasFinal[0]["cromosomas"][0], GraficasFinal[0]["cromosomas"][1], GraficasFinal[0]["cromosomas"][2], GraficasFinal[0]["cromosomas"][3], GraficasFinal[0]["cromosomas"][4],GraficasFinal[0]["cromosomas"][5],GraficasFinal[0]["cromosomas"][6]],
        "Error": aptitud
    }
    contador=contador+1
    return d1


def initialPopulation(popSize,Graficas):
    population = []
    for i in range(0, popSize):
        population.append(graficar(Graficas,i))     
    return population

#Funcion para fucionar a 2 padres para tener un hijo
def breed(parent_one_list, parent_two_list):
    # Get absolute number containing the 56 bits
    joined_number_one = 0
    for number in parent_one_list:
        joined_number_one <<= 8
        joined_number_one |= number
    joined_number_two = 0
    for number in parent_two_list:
        joined_number_two <<= 8
        joined_number_two |= number

    child_one = 1
    child_two = 1
    # while child_one == child_two:
    if(True):
        # Swap binary representation of parents
        swap_index = random.randint(1, 55)
        binary_parent_one = '{0:056b}'.format(joined_number_one)
        binary_parent_two = '{0:056b}'.format(joined_number_two)
        child_one = binary_parent_one[:swap_index] + binary_parent_two[swap_index:]
        child_two = binary_parent_two[:swap_index] + binary_parent_one[swap_index:]
        swap_bit_index = swap_index % 8
        if swap_bit_index:
            lower_bit = swap_index - swap_bit_index
            higher_bit = lower_bit + 8
            child_one = child_one[:lower_bit] + child_one[swap_index:higher_bit] + \
                        child_one[lower_bit:swap_index] + child_one[higher_bit:]
            child_two = child_two[:lower_bit] + child_two[swap_index:higher_bit] + \
                        child_two[lower_bit:swap_index] + child_two[higher_bit:]
        child_one = int(f'0b{child_one}', 2)
        child_two = int(f'0b{child_two}', 2)
    child_one_list = []
    child_two_list = []
    for i in range(len(parent_one_list)):
        value = child_one & 0xff
        if not value:
            value = 1 *5
        child_one_list.insert(0, value)
        child_one >>= 8
    for i in range(len(parent_two_list)):
        value = child_two & 0xff
        if not value:
            value = 1 *5
        child_two_list.insert(0, value)
        child_two >>= 8
    return [child_one_list, child_two_list]

def mutate(number):
    binary_value = '{0:08b}'.format(number)
    binary_list = list(binary_value)
    bit_index = random.randint(0, 7)
    if binary_list[bit_index] == '0':
        binary_list[bit_index] = '1'
    else:
        binary_list[bit_index] = '0'
    binary_value = "".join(binary_list)
    binary_value = int(binary_value, 2)
    if not binary_value:
        binary_value = 1 * 5
    return binary_value




PrimeraGeneracion=[]
ListaCromosomas=[]
individuo=[]
ListaOrdenadaCromosomas=[]
hijos=[]
SizePopulation=100
Elite=50
i=0
By=[]
Ax=[]
contador=0
PrimeraGeneracion=Inicialgraficas()
ListaCromosomas=initialPopulation(SizePopulation,PrimeraGeneracion)
Hola=[]
Next_Generation=PrimeraGeneracion
for i in range (0,150):
    hijos2=[]
    hijos=[]
    Next_Generation_Aptitud=[]
    for i in range (len(Next_Generation)):
        Next_Generation_Aptitud.append(graficar(Next_Generation,i))
    Next_Generation_Aptitud=sorted(Next_Generation_Aptitud, key=lambda d: d['Error'])
    Parent50=Next_Generation_Aptitud[:-Elite]
    for i in range (0,100,2):
      hijos+=(breed(Parent50[random.randrange(1,50)]["cromosomas"],Parent50[25]["cromosomas"]))
    for i in range (len(hijos)):
        hijo= hijos[i]
        while hijos.count(hijo)>1:
            random_number=random.randint(0,6)
            hijo[random_number]=mutate(hijo[random_number])
            hijos[i]=hijo
    for i in range (len(hijos)):
        hijos2.append(graficar(hijos,i))
    hijos2=sorted(hijos2, key=lambda d: d['Error'])
    Children50=hijos2[:-Elite]
    Graficas_finales=graficarfinal(Parent50)
    print("Mejor cromosoma" ,Graficas_finales)
    print("Generacion" ,contador)
    By.append(Parent50[0]['Error'])
    Ax.append(contador)
   
    plt.figure(2)
    plt.plot( Ax,By)
    plt.title('APTITUD')
    plt.tight_layout()
    plt.show(block=False)
    
    plt.pause(0.1)
    plt.clf()
    Next_Generation=Parent50+Children50
    Next_Generation = [value['cromosomas'] for value in Next_Generation]
    contador=contador+1
A=8
B=25
C=4
D=45
E=10
F=17
G=35
Peso=5
A2=Next_Generation[0][0]/Peso
B2=Next_Generation[0][1]/Peso
C2=Next_Generation[0][2]/Peso
D2=Next_Generation[0][3]/Peso
E2=Next_Generation[0][4]/Peso
F2=Next_Generation[0][5]/Peso
G2=Next_Generation[0][6]/Peso
    
x=[]
y=[]
x_2=[]
y_2=[]
FA=[]
aptitud = 0
i=0
while(i <= 1000):
      x.append((i+1)/10);
      y.append(A*(B*sin(x[i]/C)+D*cos(x[i]/E))+F*x[i]-G)
      x_2.append((i+1)/10);
      y_2.append(A2* (B2*sin(x_2[i]/C2)+D2*cos(x_2[i]/E2))+F2*x_2[i]-G2)
      FA.append(abs(y[i]-y_2[i]))
      i=i+1
   
plt.figure(3)
plt.plot(x,y)
plt.plot(x_2,y_2)
plt.title("Mejor ajuste de curva")
plt.tight_layout()
plt.show(block=False)
plt.pause(1)

