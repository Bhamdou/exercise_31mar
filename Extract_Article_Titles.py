import requests
from bs4 import BeautifulSoup

def fetch_webpage(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error: Unable to fetch webpage. (Status Code: {response.status_code})")
        return None

def extract_article_titles(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    article_titles = soup.find_all('h2')
    return [title.text for title in article_titles]

def main():
    url = 'https://www.example.com/news/'
    html_content = fetch_webpage(url)

    if html_content:
        article_titles = extract_article_titles(html_content)
        print("\nArticle Titles:")
        for title in article_titles:
            print(title)

if __name__ == "__main__":
    main()
