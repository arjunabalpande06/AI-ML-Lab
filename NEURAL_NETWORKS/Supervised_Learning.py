#Spam Detection

# data = [
#     #Clear Spam
#     ([1,1,0], 1),
#     ([1,0,0], 1),
#     ([0,1,0], 1),

#     #Clear Not Spam
#     ([0,0,1], 0),
#     ([0,0,0], 0),

#     #Confusing / Mixed Emails
#     ([1,0,1], 0),
#     ([0,1,1], 0),
#     ([1,1,1], 0),
#     ([0,1,0], 0),
# ]

# #Initialize Weights
# weights = [0.0, 0.0, 0.0]
# bias = 0.0
# learning_rate = 0.1
# epochs = 15
#  #Training

# for epoch in range(epochs):
#     for inputs, target in data:
#         output = 0
#         for i in range(3):
#             output += weights[i] * inputs[i]
#         output += bias

#         prediction = 1 if output >= 0 else 0
#         error = target - prediction

#         for i in range(3):
#             weights[i] += learning_rate * error * inputs[i]
        
#         bias += learning_rate * error

# #Testing on training data
# TP = FP = TN = FN = 0

# print("\nTraining data Predictions:\n")
# for inputs,target in data:
#     output = 0
#     for i in range(3):
#         output += weights[i] * inputs[i]
#     output += bias

#     prediction = 1 if output >= 0 else 0

#     print("Input:", inputs,
#           "Predicted:", prediction,
#           "Actual:",target)
#     if prediction == 1 and target == 1:
#         TP += 1
#     elif prediction == 1 and target == 0:
#         FP += 1
#     elif prediction == 0 and target == 0:
#         TN += 1
#     elif prediction == 0 and target == 1:
#         FN += 1

# #Metrics
# total = TP + TN + FP + FN
# accuracy = (TP + TN) / total
# precision = TP / (TP + FP) if (TP + FP) != 0 else 0
# recall = TP / (TP + FN) if (TP + FN) != 0 else 0
# f1 = 2 * precision * recall / (precision + recall) if (precision + recall) != 0 else 0

# print("\nConfusion Matrix:\n")
# print("                   Predicted")
# print("              ------------------")
# print("                  |spam | Not spam |")
# print("--------------------------------------")
# print("Actual Spam  |  ",TP, " |  ", FN, "   |")
# print("Actual Notspam | ", FP, "  |  ",TN, "   |")
# print("-----------------------------------------")

# print("\nEvaluation Matrics:")
# print("Accuracy :",round(accuracy, 2))
# print("Precision :",round(precision, 2))
# print("Recall :",round(recall, 2))
# print("F1 Score :",round(f1, 2))

# #User input Selection
# print("\n--- Test Your Own Email ---")
# print("Enter 1 if word is present, 0 if not.")

# free = int(input("Contains 'free'? (1/0):"))
# win = int(input("Contains 'win'? (1/0): "))
# meeting = int(input("Contains 'meeitng'? (1/0): "))

# user_input = [free, win, meeting]

# #Predict user email
# output = 0
# for i in range(3):
#     output += weights[i] * user_input[i]
# output += bias

# prediction = 1 if output >= 0 else 0

# print("\nYour Email Features : ",user_input)

# if prediction == 1:
#     print("Prediction SPAM")
# else:
#     print("Prediction : Not spam")

# <===><===><===><===><===><===><===><===><===><===><===><===><===><===><===><===><===><===><===><===><===><===><===><===><===><===><===><===><===>

# Program2 :- Loan approval
# A bank wants to predict whether a loan will be approved or rejected based on 3 features

# income_high->1 if income>threshold, else 0
# has_job->1 if employed, else 0
# credit_score_good-> 1 if credit score>threshold, else 0

#Dataset 
# data = [
#     #Clear approvals
#     ([1,1,1],1),    #High income, employed, good credit
#     ([1,1,0],1),    #High income, employed, credit not good

#     #Clear rejections
#     ([0,1,1],0),    #Low income, employed, good credit
#     ([0,0,0],0),    #Low income, umemployed, bad credit
#     ([0,1,0],0),    #Low income, umemployed, bad credit

#     #Tricky / conflicting cases
#     ([1,0,1],0),    #High income, unemployed, good credit
#     ([0,0,1],0),    #Low income, umemployed, good credit
#     ([1,0,0],1),    #High income, unempployed, bad credit

# ]

# # Initialize Weights
# weights = [0.0, 0.0, 0.0]
# bias = 0.0
# learning_rate = 0.1
# epochs = 15

# # Training
# for epoch in range(epochs):
#     for inputs, target in data:
#         output = 0
#         for i in range(3):
#             output += weights[i] * inputs[i]
#         output += bias

#         prediction = 1 if output >= 0 else 0
#         error = target - prediction

#         for i in range(3):
#             weights[i] += learning_rate * error * inputs[i]
        
#         bias += learning_rate * error


# # Testing on training data
# TP = FP = TN = FN = 0

# print("\nTraining Data Predictions:\n")
# for inputs, target in data:
#     output = 0
#     for i in range(3):
#         output += weights[i] * inputs[i]
#     output += bias

#     prediction = 1 if output >= 0 else 0

#     print("Input:", inputs,
#           "Predicted:", prediction,
#           "Actual:", target)

#     if prediction == 1 and target == 1:
#         TP += 1
#     elif prediction == 1 and target == 0:
#         FP += 1
#     elif prediction == 0 and target == 0:
#         TN += 1
#     elif prediction == 0 and target == 1:
#         FN += 1


# # Metrics
# total = TP + TN + FP + FN
# accuracy = (TP + TN) / total
# precision = TP / (TP + FP) if (TP + FP) != 0 else 0
# recall = TP / (TP + FN) if (TP + FN) != 0 else 0
# f1 = 2 * precision * recall / (precision + recall) if (precision + recall) != 0 else 0

# print("\nConfusion Matrix:\n")
# print("                      Predicted")
# print("              ------------------------")
# print("                  | Approved | Rejected |")
# print("------------------------------------------")
# print("Actual Approved  |   ", TP, "    |   ", FN, "     |")
# print("Actual Rejected  |   ", FP, "    |   ", TN, "     |")
# print("------------------------------------------")

# print("\nEvaluation Metrics:")
# print("Accuracy  :", round(accuracy, 2))
# print("Precision :", round(precision, 2))
# print("Recall    :", round(recall, 2))
# print("F1 Score  :", round(f1, 2))


# # User Input Section
# print("\n--- Test Your Own Loan Application ---")
# print("Enter 1 if condition is TRUE, 0 if FALSE.")

# income = int(input("High Income? (1/0): "))
# job = int(input("Has Job? (1/0): "))
# credit = int(input("Good Credit Score? (1/0): "))

# user_input = [income, job, credit]

# # Prediction for user input
# output = 0
# for i in range(3):
#     output += weights[i] * user_input[i]
# output += bias

# prediction = 1 if output >= 0 else 0

# print("\nYour Loan Features:", user_input)

# if prediction == 1:
#     print("Prediction: LOAN APPROVED")
# else:
#     print("Prediction: LOAN REJECTED")


#Que 3 Disease Detection(Flu prediction)
# A clinic wants to predict whether a patient has flu(1) or not (0) based on 3 features
# fever->1
# cough->1
# body_pain->1

data = [
    #Clear Flu cases
    ([1,1,1],1),
    ([1,0,1],1),
    ([0,1,1],1),

    #Clear No Flu cases
    ([0,0,0],0),
    ([1,0,0],0),
    ([0,1,0],0),

    #Tricky / mixed cases
    ([1,1,0],0),
    ([0,1,1],1),
    ([1,0,1],1),
]

# Initialize Weights
weights = [0.0, 0.0, 0.0]
bias = 0.0
learning_rate = 0.1
epochs = 15

# Training
for epoch in range(epochs):
    for inputs, target in data:
        output = 0
        for i in range(3):
            output += weights[i] * inputs[i]
        output += bias

        prediction = 1 if output >= 0 else 0
        error = target - prediction

        for i in range(3):
            weights[i] += learning_rate * error * inputs[i]

        bias += learning_rate * error


# Testing on training data
TP = FP = TN = FN = 0

print("\nTraining Data Predictions:\n")
for inputs, target in data:
    output = 0
    for i in range(3):
        output += weights[i] * inputs[i]
    output += bias

    prediction = 1 if output >= 0 else 0

    print("Input:", inputs,
          "Predicted:", prediction,
          "Actual:", target)

    if prediction == 1 and target == 1:
        TP += 1
    elif prediction == 1 and target == 0:
        FP += 1
    elif prediction == 0 and target == 0:
        TN += 1
    elif prediction == 0 and target == 1:
        FN += 1


# Metrics
total = TP + TN + FP + FN
accuracy = (TP + TN) / total
precision = TP / (TP + FP) if (TP + FP) != 0 else 0
recall = TP / (TP + FN) if (TP + FN) != 0 else 0
f1 = 2 * precision * recall / (precision + recall) if (precision + recall) != 0 else 0

print("\nConfusion Matrix:\n")
print("                    Predicted")
print("              ----------------------")
print("                | Flu | No Flu |")
print("------------------------------------")
print("Actual Flu     | ", TP, " | ", FN, " |")
print("Actual No Flu  | ", FP, " | ", TN, " |")
print("------------------------------------")

print("\nEvaluation Metrics:")
print("Accuracy  :", round(accuracy, 2))
print("Precision :", round(precision, 2))
print("Recall    :", round(recall, 2))
print("F1 Score  :", round(f1, 2))


# User Input Section
print("\n--- Test Your Symptoms ---")
print("Enter 1 if symptom is present, 0 if not.")

fever = int(input("Fever? (1/0): "))
cough = int(input("Cough? (1/0): "))
body_pain = int(input("Body Pain? (1/0): "))

user_input = [fever, cough, body_pain]

# Prediction for user input
output = 0
for i in range(3):
    output += weights[i] * user_input[i]
output += bias

prediction = 1 if output >= 0 else 0

print("\nYour Symptoms:", user_input)

if prediction == 1:
    print("Prediction: Patient HAS Flu")
else:
    print("Prediction: Patient DOES NOT have Flu")
