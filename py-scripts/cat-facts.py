# Script that makes API call to retrieve random cat facts 

import requests 

def fetch_cat_fact(): 
    response = requests.get("https://catfact.ninja/fact")
    if response.status_code == 200: 
        return response.json() # Returns a random cat fact
    else:
        return "Failed to fetch a random cat fact. Try again!"
    
if __name__ == "__main__": 
    cat_fact = fetch_cat_fact()
    print(f"Cat Fact: {cat_fact['fact']}")
