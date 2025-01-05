import ollama
import json
from os import listdir
from os.path import join
from datetime import datetime
from helper import *

MODEL = 'llama3.2'

def summarize_article(article):
    """
    Summarizes the given article in both long and short formats.
    Args:
        article (dict): A dictionary containing the article with keys 'title' and 'content'.
    Returns:
        tuple: A tuple containing two elements:
            - summary_long (str): A detailed summary of the article.
            - summary_short (str): A brief summary of the article in two sentences.
    """
    prompt_long = '''Summarize the following article, don't use markdown formatting. The viewer already knows your summary is about the article.:
    Title: {}
    Content: 
    {}'''.format(article['title'], article['content'])

    prompt_short = '''Summarize the following article in 2 scentances. Don't use markdown formatting. The viewer already knows your summary is about the article.:
    Title: {}
    Content: 
    {}'''.format(article['title'], article['content'])

    summary_long = ollama.generate(MODEL, prompt_long)
    summary_short = ollama.generate(MODEL, prompt_short)
    
    return summary_long['response'], summary_short['response']

def summarize_articles(type):
    """
    Summarizes articles of a given type by reading them from a specified directory,
    generating long and short summaries, and saving the summaries back to the files.

    Args:
        type (str): The type of articles to summarize. This should correspond to a subdirectory
                    under the articles directory named with the current date.

    Raises:
        FileNotFoundError: If the specified directory or any article file does not exist.
        json.JSONDecodeError: If an article file contains invalid JSON.

    Example:
        summarize_articles('sports')
    """
    path = '../articles/{}/{}'.format(datetime.today().strftime('%Y-%m-%d'), type)
    articles = listdir(path)
    for index, article in enumerate(articles):
        printf('Summarizing {} of {}:'.format(index+1, len(articles)), article)
        with open(join(path, article), 'r') as f:
            file_data = json.load(f)
        summary_long, summary_short = summarize_article(file_data)

        file_data['summary_long'] = summary_long
        file_data['summary_short'] = summary_short

        with open(join(path, article), "w") as file:
            json.dump(file_data, file)

def daily_summary():
    """
    Generates a daily summary of news articles for Canada and international categories.
    This function reads the summaries from a file if they exist for the current date.
    If not, it reads the articles from the respective directories, generates summaries
    using the ollama model, and saves the summaries to a file.
    Returns:
        tuple: A tuple containing the summary for Canada and the summary for international news.
    Raises:
        FileNotFoundError: If the articles directory or files are not found.
    """
    try:
        with open('../data/daily_summary.txt', 'r') as f:
            summaries = json.load(f)
    except FileNotFoundError:
        summaries = {}

    if datetime.today().strftime('%Y-%m-%d') not in summaries.keys():
        path = '../articles/{}/{}/'.format(datetime.today().strftime('%Y-%m-%d'), 'canada')
        articles = listdir(path)
        canada_data = []
        for article in articles:
            with open(join(path, article), 'r') as f:
                file_data = json.load(f)
                canada_data.append(file_data['summary_long'])
        
        path = '../articles/{}/{}/'.format(datetime.today().strftime('%Y-%m-%d'), 'international')
        articles = listdir(path)
        international_data = []
        for article in articles:
            with open(join(path, article), 'r') as f:
                file_data = json.load(f)
                international_data.append(file_data['summary_long'])
        
        canada_summaries = ''
        for summary in canada_data:
            canada_summaries += '\n\n' + summary
        
        international_summaries = ''
        for summary in international_data:
            international_summaries += '\n\n' + summary
        
        canada_summary = ollama.generate(MODEL, "Summarize all of these articles in one paragraph, The viewer already knows your summary is about. " + canada_summaries)
        international_summary = ollama.generate(MODEL, "Summarize all of these articles in one paragraph, The viewer already knows your summary is about. " + international_summaries)

        summaries[datetime.today().strftime('%Y-%m-%d')] = {}
        summaries[datetime.today().strftime('%Y-%m-%d')]['canada'] = canada_summary['response']
        summaries[datetime.today().strftime('%Y-%m-%d')]['international'] = international_summary['response']

        with open('../data/daily_summary.txt', 'w') as f:
            json.dump(summaries, f)

        return canada_summary['response'], international_summary['response']
    else:
        return summaries[datetime.today().strftime('%Y-%m-%d')]['canada'], summaries[datetime.today().strftime('%Y-%m-%d')]['international']


if __name__ == '__main__':
    printf('Started Summarizing Canadaian Articles')
    summarize_articles('canada')
    printf('Started Summarizing International Articles')
    summarize_articles('international')
    printf('Started Daily Summaries')
    printf(daily_summary())
    printf('Completed AI Bootup Sequence')
