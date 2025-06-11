# https://slothbytes.beehiiv.com/p/federated-learning

import math

def fact_of_fact(x):
    result = 1
    for i in range(1,x+1):
        result *= math.factorial(i)
    return result

print(fact_of_fact(int(input("Enter the number: "))))
