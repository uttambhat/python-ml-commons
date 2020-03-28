import numpy as np

def prepare(time_series_data,number_of_delays,test_fraction):
    time_series_length = time_series_data.shape[0]
    train_length = np.int((1.-test_fraction)*time_series_length)-(number_of_delays+1)
    test_length = time_series_length-train_length-2*(number_of_delays+1)
    
    X_train = []
    for i in range(number_of_delays):
        X_train.append(time_series_data[i:train_length+i])
    
    X_train = (np.atleast_3d(np.array(X_train).T))
    y_train = (np.atleast_2d(time_series_data[number_of_delays:train_length+number_of_delays]).T)
    
    X_test = []
    for i in range(number_of_delays):
        X_test.append(time_series_data[train_length+number_of_delays+1+i:train_length+number_of_delays+1+i+test_length])
    
    X_test = (np.atleast_3d(np.array(X_test).T))
    y_test = (np.atleast_2d(time_series_data[train_length+2*number_of_delays+1:train_length+2*number_of_delays+1+test_length]).T)
    
    return X_train,y_train,X_test,y_test

