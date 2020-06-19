import numpy as np
##### incomplete #############

def rmsprop(objective_function,theta_initial,bounds):     
    theta=theta_initial
    epochs=10000
    for i in range(epochs):
        (value,gradient)=objective_function(theta)
        
        loss_vector.append(loss)
        if i==0:
            Eg2 = np.power(grad,2)
        else:
            Eg2 = 0.9*Eg2 + 0.1*np.power(grad,2)
        
        delta_theta = self.learning_rate*grad/np.power(Eg2 + 1.e-8,0.5)
        theta = theta + delta_theta

