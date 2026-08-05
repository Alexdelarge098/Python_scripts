import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = soup.find_all('h2')  # Example: scraping all h2 headlines

    for idx, headline in enumerate(headlines,1):
       print(f"{idx}: {headline.text.strip()}")

if __name__ == "__main__":
    url = input("Enter the URL of the website to scrape: ")
    scrape_website(url)

