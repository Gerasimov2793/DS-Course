'''Guess number'''
import numpy as np
number = np.random.randint(1, 101) # Generate random numbers
count = 0 

while True:
    count += 1
    predict_number = int(input("Guess number from 1 till 100 "))
    if predict_number > number:
        print("The Number have to be smaller")
    elif predict_number < number:
        print("The Number have to be bigger")
    else:
        print(f"You have guessed correct the number! This number = {number}, after {count} tries")
        break
