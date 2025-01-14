import requests
from bs4 import BeautifulSoup

def scrape_meta_tags(url):
    try:
        # Send a GET request to the website
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find all meta tags on the page
            meta_tags = soup.find_all('meta')
            
            # Create a dictionary to store the meta tags
            meta_data = {}
            
            # Loop through each meta tag and extract its attributes
            for tag in meta_tags:
                attrs = tag.attrs
                
                # Check if the meta tag has a 'name' attribute
                if 'name' in attrs:
                    meta_data[attrs['name']] = attrs.get('content', '')
                
                # Check if the meta tag has a 'property' attribute (for OpenGraph tags)
                elif 'property' in attrs:
                    meta_data[attrs['property']] = attrs.get('content', '')
            
            return meta_data
        
        else:
            print(f"failed to retrieve the webpage. status code: {response.status_code}")
            return None
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
        

while True:
	url = input("Enter a url: https://")
	# usage
	# url = "https://treasureuzoma.brimble.app"

	meta_data = scrape_meta_tags("https://" + url)
	
	if meta_data:
		for key, value in meta_data.items():
			print(f"{key}: {value}")