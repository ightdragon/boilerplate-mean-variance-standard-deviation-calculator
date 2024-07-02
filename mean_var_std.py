import numpy as np

def calculate(list):

    np_array = np.array(list)
    
    if(np_array.size < 9):
        raise ValueError('List must contain nine numbers.')
    
    np_array_reshape = np.reshape(list, (3,3))
    #print(np_array_reshape)

    #mean
    mean_zero = np.mean(np_array_reshape, axis=0).tolist()
    mean_one = np.mean(np_array_reshape, axis=1).tolist()
    mean = np.mean(np_array_reshape).tolist()

    #variance
    var = np.var(np_array_reshape).tolist()
    var_zero = np.var(np_array_reshape, axis=0).tolist()
    var_one = np.var(np_array_reshape, axis=1).tolist()

    #standard deviation
    std = np.std(np_array_reshape).tolist()
    std_zero = np.std(np_array_reshape, axis=0).tolist()
    std_one = np.std(np_array_reshape, axis=1).tolist()

    #max
    max = np.max(np_array_reshape).tolist()
    max_zero = np.max(np_array_reshape, axis=0).tolist()
    max_one = np.max(np_array_reshape, axis=1).tolist()

    #min
    min = np.min(np_array_reshape).tolist()
    min_zero = np.min(np_array_reshape, axis=0).tolist()
    min_one = np.min(np_array_reshape, axis=1).tolist()

    #sum
    sum = np.sum(np_array_reshape).tolist()
    sum_zero = np.sum(np_array_reshape, axis=0).tolist()
    sum_one = np.sum(np_array_reshape, axis=1).tolist()

    calculations = {
        'mean': [mean_zero, mean_one, mean],
        'variance': [var_zero, var_one, var],
        'standard deviation': [std_zero, std_one, std],
        'max': [max_zero, max_one, max],
        'min': [min_zero, min_one, min],
        'sum': [sum_zero, sum_one, sum]
    }
    return calculations
    