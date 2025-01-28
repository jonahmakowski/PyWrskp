from flask import Flask, jsonify, render_template
from ai_summary import *
from get_news_data import *
from datetime import datetime
from flask_apscheduler import APScheduler
from threading import Thread

app = Flask(__name__)
log_clear()

# Configure the scheduler
class Config:
    SCHEDULER_API_ENABLED = True

started = False

app.config.from_object(Config)
scheduler = APScheduler()

def startup():
    """
    Initializes and starts a new thread to run the startup_helper function.

    This function creates a new thread with the target set to the 
    startup_helper function and starts the thread.

    Returns:
        None
    """
    x = Thread(target=startup_helper)
    x.start()

def startup_helper():
    """
    Helper function to fetch, scrape, and summarize news headlines.
    This function performs the following steps:
    1. Fetches Canadian and international news headlines.
    2. Prints the fetched headlines.
    3. Scrapes articles based on the fetched headlines.
    4. Summarizes the scraped articles.
    5. Prints daily summaries.
    The function calls the following helper functions:
    - fetch_headlines_canada(): Fetches Canadian news headlines.
    - fetch_headlines_international(): Fetches international news headlines.
    - scrape_articles(headlines, region): Scrapes articles for the given headlines and region.
    - summarize_articles(region): Summarizes articles for the given region.
    - daily_summary(): Generates a daily summary of the news.
    Note:
    - The function uses `printf` to print messages to the console.
    - Ensure that the helper functions are defined and imported correctly.
    Returns:
    None
    """
    global started
    canadian_headlines = fetch_headlines_canada()
    internationl_healines = fetch_headlines_international()
    printf('Canadian Headlines:')
    for article in canadian_headlines:
        printf(f"{article['title']}")
    
    printf('\n\n\nInternational Headlines')
    for article in internationl_healines:
        printf(f"{article['title']}")
    
    printf('\n\n\nScraping Articles')

    try:
        len_files = len(listdir(f'../articles/{datetime.today().strftime('%Y-%m-%d')}/canada'))
        len_files += len(listdir(f'../articles/{datetime.today().strftime('%Y-%m-%d')}/international'))
    except FileNotFoundError:
        len_files = 0

    if len_files == 0:
        x1 = Thread(target=scrape_articles, args=(canadian_headlines, 'canada',))
        x2 = Thread(target=scrape_articles, args=(internationl_healines, 'international',))
        x1.start()
        x2.start()
        x1.join()
        x2.join()
    else:
        printf('Scraping skipped, {} files stored.'.format(len_files))

    x1 = Thread(target=summarize_articles, args=('canada',))
    x2 = Thread(target=summarize_articles, args=('international',))
    printf('Summarizing Articles; All data scraped')
    printf('Started Summarizing Canadaian Articles')
    x1.start()
    printf('Started Summarizing International Articles')
    x2.start()
    x1.join()
    x2.join()
    printf('Started Daily Summaries')
    printf(daily_summary())
    printf('Completed AI Bootup Sequence')
    started = True

def load_data(date=datetime.today().strftime('%Y-%m-%d')):
    """
    Load and process article data for a given date.
    This function reads article files from specified directories for 'canada' and 'international' regions,
    processes the data, and adds a 'region' key to each article. It also generates daily summaries for both
    regions and returns the combined data.
    Args:
        date (str): The date for which to load articles, formatted as 'YYYY-MM-DD'. Defaults to today's date.
    Returns:
        dict: A dictionary containing processed article data and summaries with the following structure:
            {
                'articles': [
                    {
                        'title': str,
                        'content': str,
                        'region': str,
                        ...
                    },
                    ...
                ],
                'canada_summary': str,
                'international_summary': str
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

@app.route('/')
def index():
    """
    Renders the index page with data for today's date if the application has started.

    If the application has started, this function:
    - Retrieves today's date.
    - Loads data for today's date.
    - Checks if data is available for today.
    - Renders the index page with the data if available.
    - Returns a message if data is not available for today.

    If the application has not started, it returns a loading message.

    Returns:
        str: Rendered HTML template with data or a message indicating the status.
    """
    if started:
        # Get today's date
        today = datetime.today().strftime('%Y-%m-%d')

        # Load data for today (can adjust this for previous day logic)
        data = load_data(today)

        # If data is not available for today, handle appropriately
        if not data:
            return f"No data available for {today}. Try again later."

        # Render the index page and pass the data
        return render_template("index.html", data=data, today=today)
    else:
        return "Loading data..."

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
    startup()
    app.run(host='0.0.0.0', port=5001)