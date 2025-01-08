""" Dog Breed Quiz API Integration"""

import requests 
import os 
from dotenv import load_dotenv, dotenv_values
import Dog_Breed_Quiz


# Dictionary of stored values from Dog_Breed_Quiz script
quiz_data = {
    "min_weight": Dog_Breed_Quiz.min_weight,
    "max_weight": Dog_Breed_Quiz.max_weight,
    "min_height": Dog_Breed_Quiz.min_height,
    "max_height": Dog_Breed_Quiz.max_height,
    "shedding": Dog_Breed_Quiz.shedding,
    "barking": Dog_Breed_Quiz.barking,
    "protectiveness": Dog_Breed_Quiz.protectiveness,
    "energy": Dog_Breed_Quiz.energy,
    "trainability": Dog_Breed_Quiz.trainability
}

def match_score(breed, quiz_data):
    """ Calculate a percent match score based on quiz data. """
    score = 0
    total_criteria = len(quiz_data)

    # Average height for male and female dogs
    avg_min_height = (breed['min_height_male'] + breed['min_height_female']) / 2
    avg_max_height = (breed['max_height_male'] + breed['max_height_female']) / 2

    # Check if breed's height range matches the quiz's height range
    if avg_min_height <= quiz_data['max_height'] and avg_max_height >= quiz_data['min_height']:
        score += 1
    
    # Average weight for male and female dogs
    avg_min_weight = (breed['min_weight_male'] + breed['min_weight_female']) / 2
    avg_max_weight = (breed['max_weight_male'] + breed['max_weight_female']) / 2

    # Check if breed's weight range matches the quiz's weight range
    if avg_min_weight <= quiz_data['max_weight'] and avg_max_weight >= quiz_data['min_weight']:
        score += 1
    
    # Check other parameters similarly...
    if breed['shedding'] == quiz_data['shedding']:
        score += 1
    if breed['barking'] == quiz_data['barking']:
        score += 1
    if breed['protectiveness'] == quiz_data['protectiveness']:
        score += 1
    if breed['energy'] == quiz_data['energy']:
        score += 1
    if breed['trainability'] == quiz_data['trainability']:
        score += 1

    return score / total_criteria

def dog_breed_results(api_key, quiz_data, match_threshold=0.2):
    """ Obtain resulting dog breeds from Dogs API and return partially matching ones. """
    
    url = "https://api.api-ninjas.com/v1/dogs"
    headers = {"X-Api-Key": api_key}
    
    # Create params dictionary by indexing into quiz_data
    params = {
        "min_weight": quiz_data["min_weight"],
        "max_weight": quiz_data["max_weight"],
        "min_height": quiz_data["min_height"],
        "max_height": quiz_data["max_height"],
        "shedding": quiz_data["shedding"],
        "barking": quiz_data["barking"],
        "protectiveness": quiz_data["protectiveness"],
        "energy": quiz_data["energy"],
        "trainability": quiz_data["trainability"]
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        
        # Check if the response contains valid data
        breeds = response.json()
        if not isinstance(breeds, list):  # Validate the expected structure
            raise ValueError("Invalid response format")
        
        # Filter breeds based on match score threshold
        matched_breeds = [
            breed for breed in breeds 
            if match_score(breed, quiz_data) >= match_threshold
        ]
        
        return matched_breeds

    except requests.exceptions.RequestException as e:
        print(f"Error fetching dog breeds: {e}")
        return []
    except ValueError as e:
        print(f"Data error: {e}")
        return []

load_dotenv()
api_key = os.getenv("X-Api-Key")

if not api_key:
    print("API Key not found in environment variables.")
else:
    matched_dogs = dog_breed_results(api_key, quiz_data)

    if matched_dogs:
        print("Based on your preferences, you may want to adopt a: ")
        for dog in matched_dogs:
            print(f"- {dog['name']}")
    else:
        print("No matches found.")
