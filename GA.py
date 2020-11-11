from math import cos, pi
import numpy as np


def fitness(x: np.ndarray, a: int, omega: float) -> float:
    result = 0
    result = x * x - a * np.cos(omega * x)
    result = x.shape[1] * a + np.sum(result, axis=1)
    return result
    # for x in X:
    #     result += x * x - a * cos(omega * x)
    # return len(X) * a + result


def mutation(x: np.ndarray, *, percent_affected: float) -> np.ndarray:
    y = x
    for i in range(round(x.shape[0] * percent_affected)):
        index_affected = round(float(np.random.uniform(low=0, high=x.shape[1] - 1, size=1)))
        print(f'Row {i} before mutation:\n{y[i]}')
        y[i, index_affected] = np.random.uniform(low=-5.12, high=5.12, size=1)
        print(f'Row {i} after mutation {index_affected} is mutated:\n{y[i]}')
    return y


def crossover(x: np.ndarray) -> np.ndarray:
    res = x
    if x.shape[0] % 2:
        pass
        res[:-1:2], res[1::2] = np.hstack((res[:-1:2, :3], res[1::2, 3:])), \
                                np.hstack((res[1::2, :3], res[:-1:2, 3:]))

    else:
        res[::2], res[1::2] = np.hstack((res[::2, :3], res[1::2, 3:])), \
                              np.hstack((res[1::2, :3], res[::2, 3:]))
    return res


# def select_best(x: np.ndarray, *, amp: float, omg: float, procent: float)->np.ndarray:
#     y = x
#     fit = fitness(val, amp, omg)
#     tuple = [(l, i) for i, l in enumerate(fit)]
#     first = lambda x: x[0]

val = np.random.uniform(low=-5.12, high=5.12, size=(5, 5))
print(val, end='\n#####\n')
# print(val[1:-1:2])
# cros = crossover(val)
# print(cros)
omg = 2 * pi
amp = 10

fit = fitness(val, amp, omg)
tuple = [(l, i) for i, l in enumerate(fit)]
first = lambda x: x[0]
print(tuple)
tuple.sort(key=first)
print(tuple)
