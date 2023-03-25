"""Game: Guess the correct number
The PC should find the number"""
import numpy as np
def random_predict(number:int=1) -> int:
    """Generation of random numbers

    Args:
        number (int, optional): Guessed number. Defaults to 1.

    Returns:
        int: Number of trials
    """
    count = 0 
    #print(number)
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        #print(predict_number)
        if number == predict_number:
            break   
    return(count)

#number = np.random.randint(1, 51)
print(f"Number of total trials: {random_predict()}")

def score_game(random_predict) -> int:
    """avergage guess after 1000 trials 

    Args:
        random_predict (_type_): function guesses

    Returns:
        int: average amount of trials
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    print(random_array)
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f"Average number trials is: {score}")
    return(score)

# Run
if __name__ == '__main__':
    score_game(random_predict)
