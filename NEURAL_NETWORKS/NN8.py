# target_temp = 22.0  #Target temperature in celsiud
# room_temp = 20.0 #Initial room temperatue
# heater_setting = 5.0    #Intial heater power
# learning_rate = 0.1
# x=1

# #Simulation parameter 
# max_iterations = 20 #Maximum steps to run
# print("Step|Room Temp|Error|Heater|Net Heater Setting")
# print("-"*50)

# for step in range(1, max_iterations+1):
#     #Step 1:Calculate error
#     error = target_temp-room_temp

#     #Step 2:Update heater setting
#     delta_w=learning_rate*error*x
#     heater_setting+=delta_w

#     #Step 3: Approximate new rooom temperature
#     #Using scaling factor to show effect of heater (for simulation)
#     room_temp+=delta_w*5

#     #Stop if room temperature is close enough to target 
#     if abs(target_temp - room_temp) < 0.01:
#         room_temp = target_temp

#     #Display the results
#     print(f"{step:^4} | {room_temp:^9.2f} | {error:^5.2f} | {delta_w:^7.2f} | {heater_setting:^16.2f}")

#     #Stop simulation if target is reached
#     if room_temp == target_temp:
#         break


#Program 2 : Throwing a Paper into a Trash Can

#parameters
# target_distance = 3.0 #meters
# curr_distance = 0.0
# throw_strength = 2.0 #initial throw strength
# learning_rate = 0.2 #eta
# input_strength = 1.0 #x
# num_throws =30 #number of throws to simulate
# x=1
# for step in range(1, num_throws+1):
#     error = target_distance-curr_distance
#     delta_w = learning_rate*error*input_strength
#     throw_strength += delta_w
#     curr_distance+=delta_w*2
#     if abs(target_distance-curr_distance)<0.01:
#         curr_distance = target_distance
#     print(f"{step:^4}|{curr_distance:^9.2f}|{error:^5.2f}|{delta_w:^7.2f}|{throw_strength:^16.2f}")
#     if curr_distance == target_distance:
#         break


# Program 3 : Pouring Water into a Cup

# Parameters
target_volume = 250.0   # ml
hand_tilt = 10.0        # initial hand tilt units
learning_rate = 0.3    # eta
input_tilt = 1.0       # x
num_pours = 30          # number of pours to simulate
tolerance = 0.1         # acceptable error in ml

print("Pour\tTilt\t\tVolume\t\tError")

for pour in range(1, num_pours + 1):
    # predicted volume (simple linear model)
    volume = hand_tilt * input_tilt

    # error between desired and actual volume
    error = target_volume - volume

    # display results
    print(f"{pour}\t{hand_tilt:.3f}\t\t{volume:.3f}\t\t{error:.3f}")

    
    if abs(error) <= tolerance:
        print("\n Target volume reached within tolerance!")
        break

    # learning rule: adjust hand tilt
    hand_tilt += learning_rate * error * input_tilt


