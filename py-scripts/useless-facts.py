# Script that makes API request for a useless fact (no API key is required)

import requests

def get_useless_fact(): 
    response = requests.get("https://uselessfacts.jsph.pl/random.json")
    if response.status_code == 200: 
        return response.json() # Return fact
    else: 
        return "Failed to fetch a fact. Try again!"
    
if __name__ == "__main__": 
    fact = get_useless_fact()
    print(f"Fact: {fact['text']}")
