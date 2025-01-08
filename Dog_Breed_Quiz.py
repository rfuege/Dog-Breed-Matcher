"""Dog Breed Matching Quiz"""

def get_scale_val(scale_prompt):
    """ Handles logic for quiz questions involving numeric scales. """
    try:
        scale_val = int(input(scale_prompt))
        if 1 <= scale_val <= 5: 
            return scale_val
        else: 
            while scale_val < 1 or scale_val > 5:
                print('Error: number out of range. Please try again.')
                scale_val = int(input(scale_prompt))
        return scale_val
    except ValueError:
        print('Error: Please enter a valid number')
        return get_scale_val(scale_prompt)

def get_min_max_vals(min_prompt, max_prompt):
    """ Handles logic for quiz questions that ask for minimum and maximum values. """
    try: 
        min_val = int(input(min_prompt))
        max_val = int(input(max_prompt))
        
        if min_val <= max_val:
            return min_val, max_val
        else:
            while min_val > max_val: 
                print('Error: minimum cannot be greater than maximum')
                min_val = int(input(min_prompt))
                max_val = int(input(max_prompt))
        
        return min_val, max_val
    except ValueError: 
        print('Error: Please enter a valid number.')
        return get_min_max_vals(min_prompt, max_prompt)


# Question 1
min_weight, max_weight = get_min_max_vals('Enter a minimum weight for your dog in lbs. ', 'Enter a maximum weight for your dog in lbs: ')

# Question 2
min_height, max_height = get_min_max_vals('Enter a minimum height for your dog in inches.  ', 'Enter a maximum height for your dog in inches. ')

# Question 3
shedding = get_scale_val('On a scale of 1-5, how much shedding are you able to handle? (1 = little/no shedding, 5 = furnado) ')

# Question 4 
barking = get_scale_val('On a scale of 1-5, how much barking do you mind? (1 = little/no barking, 5 = very vocal)')

# Question 5 
protectiveness = get_scale_val('On a scale of 1-5, how protective do you want your dog to be? (1 = little alerting to strangers , 5 = very alert to strangers) ')

# Question 6 
energy = get_scale_val('On a scale of 1-5, how energetic would you like your dog to be? (1 = couch potato, 5 = very energetic)')

# Question 7
trainability = get_scale_val('On a scape of 1-5, how trainable would you like your dog to be? (1 = very difficult to train, 5 = very easy to train)')
