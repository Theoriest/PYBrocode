#declare the inputs and weights
height = [16.8,13.2,9.4,8.1]
mass = [121,114,210,195]
data = []
weights = [-1230,-30,300]

#prepare data for entry into neuron
for i in range(len(height)):
    data.append([1,mass[i],height[i]])

data = np.array(data)

#print out the set of inputs to the neuron
print(data)

#define function for working out output per set input
def output_calculation (data,weights):
    #declare local variables
    output = 0

    #Iterate over all sets of inputs
    for d in data :
        entry= d

        #iterate over one set of input to find output
        for e in range(len(entry)):
            output += entry[e] * weights[e]

        #find value after activation
        value = 1 if  output > 0 else 0
        output = 0

        print(value)

output_calculation(data,weights)

