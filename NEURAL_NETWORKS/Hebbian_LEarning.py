# # initial parameter
# learning_rate = 0.1
# weight = 0.5

# # Training data
# training_data = [
#     (1,1),
#     (1,1),
#     (1,0),
#     (0,1),
#     (1,1)
# ]

# print("Hebbian Learning")
# print("====================================")
# print("Initial weight: ",weight)
# print()

# # Process

# for i, (x, y) in enumerate(training_data, start=1):
#     delta_w = learning_rate * x * y
#     weight += delta_w

#     print(f"Step {i}")
#     print(f"Input {x} = {x}, Output {y} = {y}")
#     print(f"Δw = {learning_rate} x {x} x {y} = {delta_w}")
#     print(f"Updated weight : {weight}")
#     print("----------------------------------------------------")

# print("Final weight after hebbian learning : ",weight)
# print("---------------------------------------")

# test_x = int(input("Enter rest input x (1 or 0): "))
# test_y = weight*test_x
# print(f"Predicted value y = weight * test_x = {weight} * {test_x} = {test_y}")


# =========================================================================================================================================================================


# learning_rate = 0.1
# weight = 0.0

# data = [
#     (1,1),
#     (1,0),
#     (0,1),
#     (1,1),
#     (0,0)
# ]

# print("Hebbian Learning : Study -> Good Marks")
# print("----------------------------------------------------------")
# print("Day | Studied | Good Marks | Weight")
# print("-------------------------------------------------------------")


# for day, (studied, good_marks) in enumerate(data, start=1):
#     delta_w = learning_rate * studied * good_marks
#     weight += delta_w
#     print(f"{day:^3} | {studied:^7} | {good_marks:^10} | {weight:^.2f}")


# print("------------------------------------------------------")
# print(f"Final learned rate : {weight:.2f}")
# print("-------------------------------------------------------")

# print("\nTest new input")
# test_input = int(input("Did the student studied : "))
# predicted_out = weight * test_input
# print(f"\nPredicted good marks value : {weight:.2f} * {test_input} = {predicted_out}")

# if predicted_out > 0:
#     print("Chances of getting good marks")
# else:
#     print("Low chances of good marks")

# =========================================================================================================================================================================


#Exercise->Energy level
# Problem: A person exercises and feels energetic
#Input:Exercise done today(1 = yes, 0 = no)
#Output"Energy felt(1= yes, 0= no)
#Learning rate: 0.2

# #parameters
# learning_rate = 0.2
# weight = 0.0 #initial association weight

# #Simulate 7 days of data (input, output)
# #1 = yes, 0 = no
# data = [
#     (1,1),  #exercised, felt energetic
#     (0,1),  #no exercise, felt energetic
#     (1,0),  #exercised, no energy
#     (1,1), # exercised, felt energetic
#     (0,0),  #no exericse, no energy
#     (1,1),  # exercised, felt energetic
#     (0,1)   #no exercise, felt energetic
# ]

# print("Day | Exercise done | Feel Energetic | Weight")
# print("---------------------------------------")

# #Training phase
# for day, (Exercise_done, Feel_energetic) in enumerate(data, start = 1):
#     delta_w = learning_rate * Exercise_done * Feel_energetic
#     weight += delta_w
#     print(f"{day:^3} | {Exercise_done:^7} | {Feel_energetic:^10} | {weight:.2f}")

# print("------------------------------------------")
# print(f"Final Leraned Weight: {weight:.2f}")
# print("------------------------------------------")

# #Testing phase
# print("\nTesting New Input")
# test_input = int(input("Did the Person exercise? (1 = Yes, 0 = No): "))

# #Prediction using learned weight
# predicted_output = weight * test_input

# print(f"\nPredicated Good Marks Value = {weight:.2f} * {test_input} = {predicted_output:.2f}")

# #Optional interpretation
# if predicted_output > 0:
#     print("Prediction: Higher chance of feeling energetic.")
# else:
#     print("Prediction: Low chance of feeling energetic.")


# =========================================================================================================================================================================

# Songs

# 6 years experience (input, output)

learning_rate = 0.15
weight = 0.0

experience = [
    (1,1),
    (1,0),
    (0,1),
    (1,1),
    (0,0),
    (1,1)
]

print("Day | Songs Heard | Feeling | Weight")
print("---------------------------------------------------------------")



# =========================================================================================================================================================================

# Coffee -> Alertness
learning_rate = 0.15
weight = 0.0

daily_experience = [
    (1,1),
    (1,0),
    (0,1),
    (1,1),
    (0,0)
]


# =========================================================================================================================================================================

# Traffic Light -> Action

learning_rate = 0.1
weight = 0.0
# 5 trials of experiences (green light, pressed accelerator)

trials = [
    (1,1),
    (1,0),
    (0,1),
    (1,1),
    (0,0)
]