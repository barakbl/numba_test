import timeit
from numba import njit

'''
based on code from = https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/
'''

@njit
def towerOfHanoiNumba(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return None
    towerOfHanoiNumba(n-1, from_rod, aux_rod, to_rod)
    #print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    towerOfHanoiNumba(n-1, aux_rod, to_rod, from_rod)

out = []
def towerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return None
    towerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    #print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    towerOfHanoi(n-1, aux_rod, to_rod, from_rod)

n = 25
for i in range(5):
    starttime = timeit.default_timer()
    towerOfHanoi(n, 'A', 'C', 'B')
    time1 = timeit.default_timer() - starttime
    print(f"Without Numba - runtime: {time1} seconds")

    starttime = timeit.default_timer()
    towerOfHanoiNumba(n, 'A', 'C', 'B')
    time2 = timeit.default_timer() - starttime
    print(f"With Numba - runtime: {time2} seconds")

    p = 100 - (time2 / time1 * 100)
    print(f"run time with numba is  {p:.2f}% faster")
