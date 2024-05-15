import numpy as np

def stats_average(array):
    return np.sum(array)/len(array)

def stats_squared_errors(array):
    result = 0
    for x in array:
        result += (x - stats_average(array))**2
    return result/(len(array) - 1)

if __name__ == "__main__":
    example = np.array([2,3,-2,1,5, 3])
    print(f"{stats_average(example)=}")
    print(f"{stats_squared_errors(example)=}")