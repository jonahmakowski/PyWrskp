import requests
from datetime import datetime
from bs4 import BeautifulSoup
import json
from os import makedirs, getenv
from helper import *

# Your API key
API_KEY_NEWS_API = getenv("NEWS_API_KEY")
API_KEY_GNEWS = getenv("GNEWS_API_KEY")
API_KEY_NEWSDATA = getenv("NEWSDATA_API_KEY")

def use_api(params, url):
    """
    Makes a GET request to the specified URL with the given parameters and returns the JSON response.

    Args:
        params (dict): A dictionary of query parameters to include in the request.
        url (str): The URL to which the GET request is made.

    Returns:
        dict: The JSON response from the API.
    """
    # Make the request
    response_newsAPI = requests.get(url, params=params)

    # Return JSON data
    return response_newsAPI.json()

def fetch_headlines_canada():
    """
    Fetches the latest news headlines from various Canadian news sources.

    This function aggregates news articles from three different APIs: NewsAPI, GNews, and NewsData.
    It combines the results from these APIs and removes any articles from a specific source.

    Returns:
        list: A list of dictionaries, each representing a news article. The list contains articles
              from the following sources:
              - CBC News
              - Global News
              - Toronto Star
              - The Globe and Mail
              - Toronto Sun
              - National Post
              - Ottawa Citizen
              - Other general news sources in Canada

    Note:
        The function removes articles from a specific source identified by the placeholder "[Removed]".
    """
    news_api_result = use_api({"apiKey": API_KEY_NEWS_API, "language": "en", "sources": "cbc-news,global-news,toronto-star,the-globe-and-mail,toronto-sun,national-post,ottawa-citizen", "pageSize": 100}, 'https://newsapi.org/v2/top-headlines')
    gnews_api_result = use_api({"category": "general", "lang": "en", "country": "ca", "max": 10, "apikey":API_KEY_GNEWS}, 'https://gnews.io/api/v4/top-headlines')
    newsdata_api_result = use_api({"apiKey": API_KEY_NEWSDATA, "country": "ca", "language": "en"}, 'https://newsdata.io/api/1/latest')

    results = news_api_result['articles']
    results.extend(gnews_api_result['articles'])
    results.extend(newsdata_api_result['results'])

    passed = False

    while not passed:
        passed = True
        for index, result in enumerate(results):
            if 'source' in result.keys() and result['source']['name'] == "[Removed]":
                del results[index]
                passed = False
                break

    return results

def fetch_headlines_international():
    """
    Fetches international news headlines from multiple news APIs and combines the results.

    This function retrieves top headlines from three different news APIs: NewsAPI, GNews, and NewsData.
    It combines the results from these APIs into a single list of articles. Additionally, it filters out
    any articles from sources with the name "[Removed]".

    Returns:
        list: A list of dictionaries, each representing a news article with combined results from the APIs.
    """
    news_api_result = use_api({"apiKey": API_KEY_NEWS_API, "language": "en", "pageSize": 100}, 'https://newsapi.org/v2/top-headlines')
    gnews_api_result = use_api({"category": "general", "lang": "en", "max": 10, "apikey":API_KEY_GNEWS}, 'https://gnews.io/api/v4/top-headlines')
    newsdata_api_result = use_api({"apiKey": API_KEY_NEWSDATA, "language": "en"}, 'https://newsdata.io/api/1/latest')

    results = news_api_result['articles']
    results.extend(gnews_api_result['articles'])
    results.extend(newsdata_api_result['results'])

    passed = False

    while not passed:
        passed = True
        for index, result in enumerate(results):
            if 'source' in result.keys() and result['source']['name'] == "[Removed]":
                del results[index]
                passed = False
                break

    return results

def scrape_article_content(url, type, debug=False, timeout=10):
    """
    Scrapes the main content of an article from a given URL.
    Args:
        url (str): The URL of the article to scrape.
        debug (bool, optional): If True, prints debug information. Defaults to False.
        timeout (int, optional): The timeout for the GET request in seconds. Defaults to 10.
    Returns:
        str: The main content of the article as a string, or None if the request fails.
    Raises:
        requests.exceptions.RequestException: If the request to the URL fails.
    """
    try:
        printf(f'{type}: Scraping Article:', url)
        # Send a GET request to the article URL
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers, timeout=timeout)
        if debug: printf('Request Sent')

        response.raise_for_status()  # Raise an error for failed requests
        if debug: printf('Status Check Passed')

        # Parse the webpage content with BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        if debug: printf('Soup Created')

        # Attempt to extract the main article content
        # Common tags for article text include <p>, <article>, and <div>
        paragraphs = soup.find_all("p")  # Get all paragraph tags
        if debug: printf('Data Extracted')
        
        article_content = "\n".join([p.get_text() for p in paragraphs if p.get_text()])
        if debug: printf('Parsed Data')

        return article_content
    except requests.exceptions.RequestException as e:
        printf(f"Failed to fetch article: {e}")
        return None

def scrape_articles(articles, type):
    """
    Scrapes content from a list of articles and saves the data to text files.

    Args:
        articles (list): A list of dictionaries, where each dictionary contains information about an article.
        type (str): The type/category of the articles being scraped.

    Returns:
        None

    The function performs the following steps:
    1. Iterates over each article in the provided list.
    2. Extracts the article URL from the article dictionary.
    3. Scrapes the content of the article using the `scrape_article_content` function.
    4. If the content is successfully scraped, it creates a dictionary with the article's details.
    5. Creates a directory structure based on the current date and article type.
    6. Saves the article details to a text file in the created directory.
    7. Prints a message if the article content could not be scraped.
    """
    today = datetime.today().strftime('%Y-%m-%d')
    for article in articles:
        article_url = article["url"] if 'url' in article.keys() else article['link']
        article_content = scrape_article_content(article_url, type)
        if article_content and article_content is not None:
            article_dic = {'title': article['title'], 'source': article['source']['name'] if 'source' in article.keys() else article['source_name'], 'Description': article['description'], 'url': article['url'] if 'url' in article.keys() else article['link'], 'imgurl': article['urlToImage'] if 'urlToImage' in article.keys() else None, 'content': article_content}
            makedirs(f"../articles/{today}/{type}", exist_ok=True)
            safe_title = article['title'].replace('/', '_')
            with open(f"../articles/{today}/{type}/{safe_title}.txt", "w") as file:
                json.dump(article_dic, file)
        else:
            printf(f"{type}: Failed to scrape article: {article['title']}")

# Example usage
if __name__ == "__main__":
    # Fetch headlines
    canadian_headlines = fetch_headlines_canada()
    internationl_healines = fetch_headlines_international()
    printf('Canadian Headlines:')
    for article in canadian_headlines:
        printf(f"{article['title']}")
    
    printf('\n\n\nInternational Headlines')
    for article in internationl_healines:
        printf(f"{article['title']}")
    
    printf('\n\n\nScraping Articles')
    
    scrape_articles(canadian_headlines, 'canada')
    scrape_articles(internationl_healines, 'international')
