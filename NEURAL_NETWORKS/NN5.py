#1.SIMPLE NEURON
inputs = [[0,0],[0,1],[1,0],[1,1]]
targets = [0,0,0,1]


#Initilize weights and bias
w = [0,0]
b = 0
learning_rate = 1

#Training for 5 iterations
for epoch in range(5):
    print(f"Epoch {epoch+1}")
    for i in range(len(inputs)):
        x = inputs[i]
        target = targets[i]

        #Perceptron output (step function)
        output = 1 if(w[0] * x[0] + w[1]*x[1]+b)>0 else 0


        #Weights update 

        w[0] += learning_rate * (target - output)* x[0]
        w[1] += learning_rate * (target - output) * x[1]
        b += learning_rate * (target - output)
        print(f"Input: {x},Target:{target},Output: {output},Weights: {w}, Bias: {b}")
