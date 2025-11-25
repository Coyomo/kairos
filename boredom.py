import random
import time
import os


ans_correct = 0 #accuracy counter
q_answered = 0 #number of qs answered

min = 1 #lowest num for random generator
max = 9 #highest

length = 100 #length of quiz in seconds

end_time = time.time() + length

def clear():
    os.system('clear')

clear()
while time.time() < end_time:
    random_one = random.randint(min,max)
    random_two = random.randint(min,max)

    print(f"{random_one} + {random_two} = ")

    q_answered += 1
    
    if random_one + random_two == int(input()):
        ans_correct += 1
    clear()

print(f"You got {ans_correct} out of {q_answered} in {length} seconds!")