import random as r

def main():
    pass

def output_dice(dice):
    pass


def roll_die():
    #accepts no arguements
    # generates and returns a random integers between 1-6
    
    dice = r.randint(1,6)
    
    return dice

def first_roll():
    pass

def count_frequency(dice, number):
    pass

def find_mode(dice):
    pass

def list_unmatched_dice(dice):
    pass

def reroll_one(dice, index):
    # reroll_one recieves an argument for the list of dice, and the index
    # it uses the function roll_die to reroll the index of the dice needed
    # it returns the list with the index rerolled.
    
    # call roll_die to get a number
    number = roll_die()
    
    # replace it in the list
    dice[index] = number
    
    return dice

def reroll_many(dice):
    pass