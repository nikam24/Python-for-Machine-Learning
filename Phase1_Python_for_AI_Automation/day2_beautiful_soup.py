from bs4 import BeautifulSoup 
import requests 

response = requests.get("https://www.google.com") 
title = BeautifulSoup(response.text, "html.parser").title 
print(f"Title: {title.string}")
