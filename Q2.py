# Simulate 3-door game
import random
import os

# Simulate the game N times
# Return the number of times a game player guessed correctly.
def simulate(N):
    correct_guess_count = 0
    for i in range (0, N):
        # Game organizers select a door randomly and places a car behind it
        door_with_car = select_door()
        # Game player selects a door randomly hoping that the car is behind it
        guessed_door_no = select_door()
        
        # Host opens a door that is not the car door and not the player's initial choice
        door_opened = host_opens_door(door_with_car, guessed_door_no)
        # Player switches to the remaining unopened door
        guessed_door_no = switch_choice(guessed_door_no, door_opened)
        
        # Did the player guess correctly?
        if door_with_car == guessed_door_no:
            correct_guess_count += 1
    return correct_guess_count

# Simulate the choice of the door with a car behind it
def select_door():
    # Draw a random number between 0 and 1. If between 0 and 1/3, then
    # door 1 selected, if between 1/3 and 2/3, then door 2, otherwise
    # door 3.
    r = random.random()
    if r < (1.0 / 3.0):
        return "A"
    elif r >= (1.0 / 3.0) and r < (2.0 / 3.0):
        return "B"
    # r > 2/3
    return "C"

# Simulate the host opening a door that does not have the car behind it 
def host_opens_door(door_with_car, guessed_door_no):
    doors = ["A","B","C"]
    # Host must open a door that is not the car door and not the player's choice
    remainig_doors = [door for door in doors if door != door_with_car and door != guessed_door_no]
    return random.choice(remainig_doors)
# Simulate the player switching their choice
def switch_choice(guessed_door_no, door_opened):
     doors = ["A","B","C"]
     # Player switches to the only remaining unopened door 
     for door in doors:
         if door != guessed_door_no and door != door_opened:
            return door 


N_values = [10000, 100000, 1000000]
output_lines = []
for N in N_values:
    hits = simulate(N)
    result = f"For N = {N},percentage of times guess was right after switching = %,{(100.0 * hits) / N:.2f} "
    print(result)
    output_lines.append(result)
with open("simulation_output.txt", "w") as file:
    for line in output_lines:
        file.write(line + "\n")
try : 
    if os.name == "posix": 
        os.system(f"open simulation_output.txt")
except:
    print ("could not open the file:")


