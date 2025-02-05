import requests
from bs4 import BeautifulSoup
import os

def extract_images(url):
    response = requests.get(url)
    print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.find_all('img')
    for image in images:
        print(image['src'])
        image_url = image['src']
        image_name = os.path.basename(image_url)
        image_response = requests.get(image_url)
        with open(image_name, 'wb') as f:
            f.write(image_response.content)

extract_images('http://localhost:4000/2025/02/05/RabbitMQ/')