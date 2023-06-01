import requests
import os
from bs4 import BeautifulSoup

class ScrapeWebpage():

    def __init__(self, url, headers): 
        self.url = url 
        self.headers = headers

    def get_webpage(self):
        response = requests.get(self.url,headers=self.headers)
        if response.status_code == 200:
            print('Webpage retrieved')
            html_content = response.text
        else:
            print('Request failed with status code', response.status_code)
        return html_content

    def search_content(self, html_content, attribute, value):
        soup = BeautifulSoup(html_content, 'html.parser')
        elements = soup.find_all(attrs={attribute: value})
        texts = []
        if elements: 
            for element in elements: 
                texts.append(element.text.strip())
                print(element)
            print(f"Found {len(elements)} occurrences with attribute '{attribute}' and value '{value}':")
        else: 
            print(f"No occurrences with attribute '{attribute}' and value '{value}' found")
        return texts


