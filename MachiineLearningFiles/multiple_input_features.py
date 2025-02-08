# import python modules
import numpy as np #to help with matrix multiplication

# declare the inputs and weights
height = [16.8,13.2,9.4,8.1]
mass = [121,114,210,195]
data = []
before = [] # to store values before training neuron
after = [] # to store values at final stage when testing
weights = np.array([-1230.0,-30.0,300.0])
targets = [1,1,0,0]
alpha = 0.01 #learning rate
epochs  = 9#number of iterations


# prepare data for entry into neuron
for i in range(len(height)):
    data.append([1,mass[i],height[i]])

data = np.array(data)

# define function for working out output per set input
def output_calculation (inputs,weights):
    weighted_sum = np.dot(inputs, weights) # wTx / dot product of weights and each input vector
    return 1 if weighted_sum > 0 else 0 # return value after activation 

# train using gradient Descent Algorithm
def train_neuron(data, weights, targets, learning_rate, epochs):
    for epoch in range(epochs):
            for i in range(len(data)):
                # calculate output for the current input
                output = output_calculation(data[i], weights)

                # calculate error
                error = targets[i] - output

                # update weights using gradient descent
                weights += learning_rate * error * data[i]
                print (weights)
                       

            # print weights and loss at intervals
            if epoch % 10 != 0:
                loss = np.sum((targets - np.array([output_calculation(d, weights) for d in data])) ** 2)
                print(f"Epoch {epoch}, Loss: {loss:.4f}, Weights: {weights}")
        
    return weights

# values before training
for i in range(len(data)):
   # Calculate output for the current input
    before.append(output_calculation(data[i], weights)) 
print(f"The output before traing is {before}\n\n","Training occurs modulating the weights as follows: \n")

# train the neuron
trained_weights = train_neuron(data, weights, targets, alpha, epochs)

print("\nTrained Weights are:", trained_weights,"\n")

# test the neuron to see if it matches desired output
print(f"The desired output is {targets} \n")
for i in range(len(data)):
    after.append(output_calculation(data[i], trained_weights)) 
print(f"The output after training the neuron is {after} \n")
