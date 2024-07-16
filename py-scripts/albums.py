# Script that makes an API request to my own album API hosted on Render 

import requests 

def get_random_album(): 
    response = requests.get("https://sbennett-album-api.onrender.com/api/albums/random")
    if response.status_code == 200: 
        return response.json()
    else: 
        return "Failed to fetch a random album. Try again!"
    
def log_album(album):
    with open("albums-log.txt", "a") as log_file: 
        log_file.write(f"{album['title']} by {album['artist']}, released in {album['year']}.\n")
    
if __name__ == "__main__":
    random_album = get_random_album()
    log_album(random_album)
    print(f"Random album: {random_album['title']} by {random_album['artist']}, released in {random_album['year']}.")
    