from flask import Flask, jsonify, render_template
from ai_summary import *
from get_news_data import *
from datetime import datetime
from flask_apscheduler import APScheduler

app = Flask(__name__)

# Configure the scheduler
class Config:
    SCHEDULER_API_ENABLED = True

app.config.from_object(Config)
scheduler = APScheduler()

def load_data(date=datetime.today().strftime('%Y-%m-%d')):
    """
    Load and process article data for a given date.
    This function reads article data from two directories: 'canada' and 'international',
    for the specified date. It adds a 'region' key to each article's data and combines
    all articles into a single dictionary. Additionally, it includes summary information
    for both 'canada' and 'international' articles.
    Args:
        date (str): The date for which to load articles, formatted as 'YYYY-MM-DD'.
                    Defaults to today's date.
    Returns:
        dict: A dictionary containing all articles and their respective summaries.
              The dictionary has the following structure:
              {
                  'articles': [
                      {
                          'region': 'ca' or 'in',
                          ... (other article data)
                      },
                      ...
                  ],
                  'international_summary': ...,
                  'canada_summary': ...
              }
    """
    path = '../articles/{}/{}'.format(date, 'canada')
    articles = listdir(path)
    data = {'articles': []}
    for article in articles:
        with open(join(path, article), 'r') as f:
            file_data = json.load(f)
            file_data['region'] = 'ca'
            data['articles'].append(file_data)
    
    path = '../articles/{}/{}'.format(date, 'international')
    articles = listdir(path)
    for article in articles:
        with open(join(path, article), 'r') as f:
            file_data = json.load(f)
            file_data['region'] = 'in'
            data['articles'].append(file_data)
    
    data['canada_summary'], data['international_summary'] = daily_summary()

    return data

@scheduler.task('cron', id='daily_job', hour=0, minute=0)
def get_all_articles():
    """
    Fetches and processes all articles from Canadian and international sources.
    This function performs the following steps:
    1. Fetches headlines from Canadian and international sources.
    2. Scrapes articles based on the fetched headlines.
    3. Summarizes the scraped articles.
    4. Loads the processed data into a global variable.
    Global Variables:
    data (dict): A dictionary containing the processed article data.
    Returns:
    None
    """
    global data
    canadian_headlines = fetch_headlines_canada()
    internationl_healines = fetch_headlines_international()

    scrape_articles(canadian_headlines, 'canada')
    scrape_articles(internationl_healines, 'international')
    
    summarize_articles('canada')
    summarize_articles('international')

    data = load_data()

load_data() # Load data from files on startup

@app.route('/')
def index():
    """
    Fetches and displays data for today's date on the index page.

    This function performs the following steps:
    1. Gets today's date in 'YYYY-MM-DD' format.
    2. Loads data corresponding to today's date.
    3. Checks if data is available for today.
    4. If data is not available, returns a message indicating no data is available.
    5. If data is available, renders the index page with the data and today's date.

    Returns:
        str: A message indicating no data is available for today if data is not found.
        str: Rendered HTML template for the index page with the data and today's date if data is found.
    """
    # Get today's date
    today = datetime.today().strftime('%Y-%m-%d')

    # Load data for today (can adjust this for previous day logic)
    data = load_data(today)

    # If data is not available for today, handle appropriately
    if not data:
        return f"No data available for {today}. Try again later."

    # Render the index page and pass the data
    return render_template("index.html", data=data, today=today)

@app.route("/api/<date>")
def get_data(date):
    """
    Fetches and returns data for a given date.

    Args:
        date (str): The date for which to fetch the data, in the format 'YYYY-MM-DD'.

    Returns:
        Response: A Flask Response object containing the JSON representation of the data.
    """
    data = load_data(date)
    return jsonify(data)

scheduler.init_app(app)
scheduler.start()

if __name__ == "__main__":
    app.run(host='0.0.0.0')