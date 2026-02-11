# Reddit Community Insights Bot

This is a non-commercial, educational project that connects to Reddit using the official Reddit API to analyze publicly available posts and comments from selected subreddits.

## Purpose

The bot generates aggregated insights to help improve content discoverability and community understanding. It can:

- Detect trending topics  
- Identify recurring or frequently asked questions  
- Generate structured discussion summaries  
- Produce basic analytics reports (posted only with moderator approval)  

## Why an API Key is Required

An API key (client ID and client secret) is required to:

- Authenticate the application with Reddit  
- Access public subreddit data through approved API endpoints  
- Comply with Reddit’s rate limits and Developer Terms  
- Transparently identify the application via a user agent  

## Compliance

- Only accesses publicly available data  
- Does not scrape private or deleted content  
- Does not store personal data beyond temporary processing  
- Does not automate engagement without moderator approval  

## Usage

1. Create a Reddit application: https://www.reddit.com/prefs/apps  
2. Fill in `config.py` with your credentials  
3. Install dependencies: `pip install -r requirements.txt`  
4. Run the bot: `python bot.py`  
