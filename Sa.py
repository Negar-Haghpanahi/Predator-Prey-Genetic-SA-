from os import fdopen
import numpy as np
import random
import math

f = open('F:/NEGAR UNI/term 6/AI/HW2/input.txt' , 'r')
context = f.readlines()
#INITIAL DATA & PARAMETERS
vertex_number =int(context[0])
T = 1000
t_change = 0.988
len_input = len(context)
v1 =[]

for num in range(1,len_input):
    v1.append(context[num].split(' '))



for i in range(0 , vertex_number):
    if any(i+1==x[1] for x in v1):
        flag=1
    else:
        value=i+1

def found(n):
    temp=v1[0]
    for j in range(0 , len(v1)):
        if n==v1[j][1]:
            temp=v1[j]
    return temp


# OBJECTIVE FUNCTION
def objective(sol):
    count=vertex_number
    for i in range(1,len(sol)):
        if sol[0]==value:
            count=count-1
        temp=found(sol[i])
        if sol[i]==temp[1] and sol[i-1]!=temp[0]:
            count=count-1
    return count

# INITIAL SOLUTION
solution = random.sample(range(0, vertex_number), vertex_number)
fitness = objective(solution)   

# MAIN LOOP OF SA ALGORITHM
while T > 0:
    neighbour = solution.copy()
    temp = np.random.randint(vertex_number)
    neighbour[temp] = np.random.randint(vertex_number)
    fit = objective(neighbour)

    delta = fit - fitness
    if delta >= 0:
        solution = neighbour
        fitness = fit
    else:
        pr = math.exp(delta / T)
        if pr >= .988:
            solution = neighbour
            fitness = fit

    print(fitness)
    T = int(T*t_change)


print(solution)
print(fitness)
