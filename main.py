import random
import numpy as np
import timeit
from numba import njit

'''
 0(n) - no ready for numba usage
'''
def best_buy_sell(arr : list):
    max = None
    min = lowest = arr.pop(0)
    lowest_day = 0
    for idx, value in enumerate(arr):
        if value > lowest:
            if max is None or max-lowest < value - lowest:
                max = value
                max_day = idx
                min = lowest
                min_day = lowest_day
        elif value < lowest:
                lowest = value
                lowest_day = idx
    if max:
        print(f"day: {min_day} ({min}) to day: {max_day} ({max}), profit: {max-min}")


@njit()
def best_buy_sell_numba(arr : np.array):
    max = max_day = min_day =  None
    min = lowest =  0
    lowest_day = 0
    for idx in range(arr.shape[0]):
        value = arr[idx]
        if idx == 0:
            min = lowest = value
        else:
            if value > lowest:
                if max is None or max-lowest < value - lowest:
                    max = value
                    max_day = idx
                    min = lowest
                    min_day = lowest_day
            elif value < lowest:
                    lowest = value
                    lowest_day = idx
    if max is not None:
        print(f"day: {min_day} ({min}) to day: {max_day} ({max}), profit: {max-min}")

for i in range(3):
    print(f"--- iteration {i+1} ---")
    data = [random.randint(1, 100000) for i in range(50000000)]
    starttime = timeit.default_timer()
    best_buy_sell(data)
    time1 = timeit.default_timer() - starttime
    print(f"No Numba - runtime: {time1} seconds")

    starttime = timeit.default_timer()
    data_np = np.array(data, dtype="int64")
    best_buy_sell_numba(data_np)
    time2 = timeit.default_timer() - starttime
    print(f"With Numba - runtime: {time2} seconds")
    p = 100 - (time2 / time1 * 100)
    print(f"run time with numba is  {p:.2f}% faster")
