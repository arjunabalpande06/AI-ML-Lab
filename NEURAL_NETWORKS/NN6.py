# 2.Simple Loan Eligibilty Chekcer
import math
#Training data:[income,age,target]
data = [
    [40000,25,0],
    [60000,30,1],
    [55000,20,0],
    [70000,35,1],
    [30000,22,0]
]

#Scaling factors
INCOME_SCALE = 100000
AGE_SCALE = 100

#Initialize weights and bias
w = [0,0]
b = 0
learning_rate = 1
epochs = 500 #more epochs for better training

#Sigmoid function 
def sigmoid(x):
    return 1/(1+math.exp(-x))

#Training using basic gradient descent 
for epoch in range(epochs):
    for d in data:
        income,age,target = d
        x1 = income / INCOME_SCALE
        x2 = age / AGE_SCALE
        z = w[0]*x1+w[1]*x2+b
        y = sigmoid(z)

        error = target - y
        #Weight update
        w[0] += learning_rate * error * x1 
        w[1] += learning_rate * error * x2
        b += learning_rate * error
    print("Training complete!")
    print(f"Weights:{w},Bias:{b}\n")

    #Test user input
    income = float(input("Enter your income (INR):"))
    age = int(input("Enter your age:"))

    x1 = income/INCOME_SCALE
    x2 = age/AGE_SCALE
    output = sigmoid(w[0]*x1 + w[1]*x2 + b)


    #Threshold 0.5
    if output >= 0.5:
        print("Congratulations!You are Eligible for a loan.")
    else:
        print("Sorry,you are Not Eligible for a loan.")
