#declare the inputs

data = [1,114,15.2]
weights =[-1200,-30,300]

def weight_modulation (data,weights):
    #declare variables
    expected = 1
    rate = 0.001
    output = 0


    #print each current states for the weights
    print(weights)

    #find output
    for i in range(len(data)) :
        output += data[i] * weights[i]

    #find value after activation
    value = 1 if  output > 0 else 0

    #find difference
    diff = expected - value

    #print current output and value after activation
    print(f"output from W transpose X is {output} , value after activation is {value}\n")

    if value != expected:
        for j in range(len(weights)):
            weights[j] = weights[j] + rate * diff  * data[j]
        return weight_modulation(data,weights)

    # When condition is met, round final weights to two decimal places
    weights = [round(w, 4) for w in weights]
    return weights, round(output, 2)

#call the weight modulation method
finalWeights , finalOutput = weight_modulation(data,weights)
print(f"\n\nThe final weights list is {finalWeights}")
print(f"The final output is {finalOutput}")


