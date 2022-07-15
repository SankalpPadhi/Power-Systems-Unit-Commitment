# Unit commitment problem for 4 units sharing a total load between 4 MW and 48 MW
# importing modules
from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np

# Defining generating unit parameters
a = np.array([0.385,0.80,1.0,1.25])
b = np.array([23.5,26.5,30.0,32])
minCapacity = 1
maxCapacity = 12
x = []

# Computation of load sharing among units
def f(x,p,q):
    return p*x**2 + q*x

def F1(x,p,q):
    return f(x,p,q)

def F2(x):
    i = 0
    varF2 = np.zeros(100)

    if ((x <= maxCapacity) and (x >= 2*minCapacity)):

        while (((minCapacity + i) <= maxCapacity) and ((x-(i + minCapacity)) >= minCapacity)):
            varF2[i] = f(minCapacity+i,a[1],b[1]) + F1((x-(i + minCapacity)),a[0],b[0])
            i = i +1

    elif((x > maxCapacity) and (x <= maxCapacity + minCapacity)):

        while (((minCapacity + i) <= maxCapacity) and ((x-(i + minCapacity)) >= minCapacity)):
            varF2[i] = f(minCapacity+i,a[1],b[1]) + F1((x-(i + minCapacity)),a[0],b[0])
            i = i +1

    elif((x > maxCapacity + minCapacity) and (x <= 2*maxCapacity)):

        while (((x-(maxCapacity-i)) <= maxCapacity) and ((maxCapacity-i) >= minCapacity)):
            varF2[i] = f(x-maxCapacity+i,a[1],b[1]) + F1((maxCapacity-i),a[0],b[0])
            i = i +1
    
    # Printing and plotting results when only first 2 units are operating
    # print(i)
    # print(varF2[0:i])
    # print(np.argmin(varF2[0:i]))
    # slNo = np.arange(i)
    # plt.plot(slNo,varF2[0:i])
    # plt.title("Variation of total cost against unit 2's generation")
    # plt.xlabel("Unit 2's generation in MW")
    # plt.ylabel("Total cost in Rs/hr")
    # plt.show()
    return np.min(varF2[0:i])   
   

def F3(x):
    i = 0
    varF3 = np.zeros(100)
    
    if ((x <= 2*maxCapacity ) and (x >= 3*minCapacity)):

        while (((minCapacity + i) <= maxCapacity) and ((x-(i + minCapacity)) >= 2*minCapacity)):
            varF3[i] = f((minCapacity+i),a[2],b[2]) + F2(x-(minCapacity + i))
            i = i +1

    elif((x > 2*maxCapacity) and (x <= (2*maxCapacity + minCapacity))):

        while (((minCapacity + i) <= maxCapacity) and ((x-(i + minCapacity)) >= 2*minCapacity)):
            varF3[i] = f((minCapacity+i),a[2],b[2]) + F2(x-(minCapacity + i))
            i = i +1

    elif((x > (2*maxCapacity + minCapacity)) and (x <= 3*maxCapacity)):

        while (((x-(2*maxCapacity-i)) <= maxCapacity) and ((2*maxCapacity-i) >= 2*minCapacity)):
            varF3[i] = f(x-2*maxCapacity+i,a[2],b[2]) + F2(2*maxCapacity - i)
            i = i +1
    
    # Printing and plotting results when first 3 units are operating
    # print(i)
    # print(varF3[0:i])
    # print(np.argmin(varF3[0:i]))
    # slNo = np.arange(i)
    # plt.plot(slNo,varF3[0:i])
    # plt.title("Variation of total cost against unit 3's generation")
    # plt.xlabel("Unit 3's generation in MW")
    # plt.ylabel("Total cost in Rs/hr")
    # plt.show()
    return np.min(varF3[0:i])   

def F4(x):
    i = 0
    varF4 = np.zeros(100)
     
    if ((x <= 3*maxCapacity ) and (x >= 4*minCapacity)):

        while (((minCapacity + i) <= maxCapacity) and ((x-(i + minCapacity)) >= 3*minCapacity)):
            varF4[i] = f((minCapacity+i),a[3],b[3]) + F3(x-(minCapacity + i))
            i = i +1

    elif((x > 3*maxCapacity) and (x <= (3*maxCapacity + minCapacity))):

        while (((minCapacity + i) <= maxCapacity) and ((x-(i + minCapacity)) >= 3*minCapacity)):
            varF4[i] = f((minCapacity+i),a[3],b[3]) + F3((x-(minCapacity + i)))
            i = i +1

    elif((x > (3*maxCapacity + minCapacity)) and (x <= 4*maxCapacity)):

        while (((x-(3*maxCapacity-i)) <= maxCapacity) and ((3*maxCapacity-i) >= 3*minCapacity)):
            varF4[i] = f(x-3*maxCapacity+i,a[3],b[3]) + F3(3*maxCapacity - i)
            i = i +1
    
    # Printing and plotting results when all the 4 units are operating
    print(i)
    print(varF4[0:i])
    print(np.argmin(varF4[0:i]))
    slNo = np.arange(i)
    plt.plot(slNo,varF4[0:i])
    plt.title("Variation of total cost against unit 4's generation")
    plt.xlabel("Unit 4's generation in MW")
    plt.ylabel("Total cost in Rs/hr")
    plt.show()
    return np.min(varF4[0:i])   

# Testing and plotting results for any number of units working together
testF4 = F4(18)
print(testF4)
# testF3 = F3(18)
# print(testF3)
# testF2 = F2(22)
# print(testF2)   
# testF1 = F1(9,a[0],b[0])
# print(testF1)
