#3.Daily Savings Predictor2
#Collect past savings 
savings = []
num_days = 3
for i in range(num_days):
    amount  = float(input(f"Enter savings for day {i+1} (INR) : "))
    savings.append(amount)

# Training data: inputs = previous days, target = next day savings 


#Scale inputs for better training 
MAX_SAVINGS = max(savings + [1]) #prevent division by zero 
inputs = [s / MAX_SAVINGS for s in savings]

targets = sum(inputs) / len(inputs) #next day = average

#Initialize weights and bias
w = [0.0 for _ in range (num_days)]
b = 0.0
learning_rate = 0.1
epochs = 500
#Simple linear neuron (no activation for regression)
def neuron(x, w, b):
    return sum(xi*wi for xi, wi in zip(x, w)) + b

#Training using basic gradient descent
for epoch in range(epochs):
    y_pred = neuron(inputs, w, b)
    error = targets -  y_pred
    # Update weights and bias
    for i in range(num_days):
        w[i] += learning_rate * error * inputs[i]
    b += learning_rate * error

#Predict next days savings 

pred_scaled = neuron(inputs, w, b)
pred_next_day = pred_scaled * MAX_SAVINGS
print(f"Predicted savings for next day: {pred_next_day:.2f}INR")
