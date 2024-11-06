import requests
from bs4 import BeautifulSoup

# URL of the webpage
url = "https://www.bestwordlist.com/5letterwords.html"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the <span class="mt"> elements, which contain the 5-letter words
word_spans = soup.find_all("span")

# Extract the text from the <span> elements and store them in a list
words = [span.text.strip() for span in word_spans]

# Print the list of words
print(words)