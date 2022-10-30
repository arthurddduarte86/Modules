# forma, bastante interessante pois usa um buffer pra armazenar os valores
from functools import reduce, lru_cache
from operator import mul
@lru_cache
def factorial_with_cache(number:int):
    if number == 0: return 1
    return reduce(mul, range(1, number+1))



# high_and_low("1 9 3 4 -5") # return "9 -5"
@lru_cache
def high_and_low(numbers):
    a = list(map(int, numbers.split()))
    return "{} {}".format(max(a), min(a))


# Well met with Fibonacci bigger brother, AKA Tribonacci.
@lru_cache
def tribonacci(signature, n):
    resultado= signature[:n]
    for i in range(n-3): resultado.append(sum(resultado[-3:]))
    return resultado







