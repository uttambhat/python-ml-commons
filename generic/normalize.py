import numpy as np

def normalize(x):
    x_mean = np.mean(x,axis=0)
    x_stdev = np.sqrt(np.var(x,axis=0))
    return (x-x_mean)/x_stdev,x_mean,x_stdev

