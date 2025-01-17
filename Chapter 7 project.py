import random as r

def main():
    pass

def output_dice(dice):
    pass


def roll_die():
    #accepts no arguments
    # generates and returns a random integers between 1-6
    
    dice = r.randint(1,6)
    
    return dice

def first_roll():
    #accepts no arguments
    #uses the variable dice to generate 12 random integers
    #and puts them in a list and returns them
    
    #initialize 
    dice_list = []
    index = 0
    
    #loop for 12 integers
    while index < 12:
        
        dice_list.append(roll_die())
        index += 1
        
    return dice_list
        

def count_frequency(dice, number):
    #recives an arguement for dice and number
    #Accepts a target number and the list of 12
    #counts the frequency of the number and returns the amount ocurred.
    
    #initialize the variable
    amount_occured = 0
    #loop throught the list
    for die in dice:
        if die == number:
            #add to the count
            amount_occured += 1
    #return
    return frequency
    

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


