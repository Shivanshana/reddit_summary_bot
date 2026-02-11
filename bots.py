# bot.py
import praw
from config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT
from utils import extract_trending_topics, summarize_posts

# Step 1: Connect to Reddit via API (requires API key)
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT
)

# Step 2: Select subreddit
subreddit_name = "learnpython"  # Example: programming subreddit
subreddit = reddit.subreddit(subreddit_name)

# Step 3: Fetch recent posts (limit 50 for demo)
posts = list(subreddit.new(limit=50))

# Step 4: Analyze trending topics
trending = extract_trending_topics(posts, top_n=10)
print(f"Top trending words in r/{subreddit_name}:")
for word, count in trending:
    print(f"{word}: {count} mentions")

# Step 5: Generate summary report
summary_df = summarize_posts(posts)
print("\nPost summary:")
print(summary_df.head(10))  # Display top 10 posts

# Step 6 (Optional): Post summary comment - ONLY with moderator approval
# subreddit.submit(title="Weekly Summary", selftext="...")  # Uncomment if approved
