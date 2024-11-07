"""Fetch News"""
import json
import requests

def fetch_news(api_key = 'pub_56216584c3f5292136fd35d95f948f5d80217', language = 'en'):
    """Fetch news using the newsdata.io API

    Args:
        api_key (str) : newsdata.io API keys. Default is pub_4128925dfa2a70c562b279e6cda7553c93e46
        language (en) : Language of the fetched news article. Default is English

    Returns:
        dict: JSON Dict if fetch news article was successful else
        None: If news API returned an error.
    """
    url = f'https://newsdata.io/api/1/news'
    params = {
        'apikey': api_key,
        'country': 'us',
        'language': language,
        # 'size': 10,  # Number of news article per API hit can between 1 to 50.
        'q': 'stock market'
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for 4XX or 5XX errors

        print(f"Request URL: {response.request.url}")

        # Parse the JSON response
        data = response.json()

        return data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
        return None

import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract text from the page
        # You can adjust the extraction logic based on the HTML structure of the target website
        text = soup.get_text(separator='\n')  # This gets all text in the page

        # Optionally, you can process the text to remove extra whitespace
        cleaned_text = '\n'.join(line.strip() for line in text.splitlines() if line.strip())

        return cleaned_text

    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None
    

def news_api(file_name: str):
    """Fetch News data dict and write it to JSON file

    Args:
        file_name (str) : JSON file name where the news data dict should be stored

    Returns:
        str: JSON file_name if fetch news article was successful else
        None: If news API returned an error.
    """
    # Fetch news articles
    news_data = fetch_news()

    if news_data:
        if 'results' in news_data:
            found_paid_content = False

            for article in news_data['results']:
                if 'content' in article:
                    if article['content'] == 'ONLY AVAILABLE IN PAID PLANS':
                        cleaned_text = extract_text_from_url(article["link"])
                        article["extracted text"] = cleaned_text
                    else:
                        article["extracted text"] = article['content'] 

                
        # Pretty print the response
        news_json = json.dumps(news_data, indent=4)
        with open(file_name, 'w') as fp:
            fp.write(news_json)

        return file_name

    else:
        print("Failed to fetch news data.")
        return None

if __name__ == "__main__":
    news_api('src/news_articles.json')
