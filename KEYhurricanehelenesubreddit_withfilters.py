import praw
import pandas as pd
import time

# Define keywords that indicate relevance to Hurricane Helene
positive_emotions_keywords = [
    'happy', 'joyful', 'grateful', 'thankful', 'hopeful', 'relieved',
    'excited', 'optimistic', 'content', 'satisfied', 'peaceful',
    'cheerful', 'delighted', 'elated', 'inspired', 'confident',
    'proud', 'lucky', 'blessed', 'euphoric', 'joyous', 'appreciative',
    'calm', 'thankful', 'comfortable', 'grinning', 'smiling', 'motivated',
    'uplifted', 'refreshed', 'relaxed', 'good', 'glad'
]
negative_emotions_keywords = [
    'sad', 'angry', 'frustrated', 'fearful', 'scared', 'hopeless', 'anxious',
    'depressed', 'disappointed', 'betrayed', 'guilty', 'hurt', 'nervous',
    'lonely', 'ashamed', 'heartbroken', 'desperate', 'grief', 'angst', 'upset',
    'devastated', 'terrified', 'dismayed', 'overwhelmed', 'despair',
    'miserable', 'distressed', 'shocked', 'helpless', 'vulnerable', 'isolated',
    'stressed', 'worried', 'frightened', 'discouraged', 'regretful', 'lost',
    'doom', 'bad', 'hate', 'nightmare'
]
# Neutral emotions/feelings keywords
neutral_emotions_keywords = [
    'neutral', 'indifferent', 'calm', 'bored', 'apathetic', 'indifferent',
    'detached', 'reserved', 'unmoved', 'unconcerned', 'unaffected',
    'unenthusiastic', 'unimpressed', 'moderate', 'nonchalant', 'passive',
    'unperturbed', 'balanced', 'steady', 'unexcited', 'uninvolved'
]

# Helene keywords
relevant_helene_keywords = ['helene', 'storm helene', 'evacuate', 'evacuation', 'aftermath', 'damage', 'tropical storm', 'destruction', 'damage', 'power outages', 'debris', 'power lines down', 'recovery', 'rescue', 'relief', 'shelter', 'hurricane helene', 'impact', 'effects', 'recovery', 'mental health', 'experience', 'help', 'community', 'support']

# Initialize the Reddit API client
reddit = praw.Reddit(
    client_id='R56d6atFieHcJoZqQDQQmQ',  # Replace with your client ID
    client_secret='NajuFmUCAu8FREQww0u__ag53_m0KA',  # Replace with your client secret
    user_agent='script:my_hurricane_scraper:v1.0 (by u/sjanesasha)'
)

# Helper functions
def contains_keyword(text, keywords):
    return any(keyword.lower() in text.lower() for keyword in keywords)

def get_sentiment(text):
    if contains_keyword(text, negative_emotions_keywords):
        return 'Negative'
    elif contains_keyword(text, positive_emotions_keywords):
        return 'Positive'
    else:
        return 'Neutral'

# Data storage
titles_data, posts_data, comments_data = [], [], []

# Fetch and process posts from different filters
filters = [
    lambda: reddit.subreddit('HurricaneHelene').new(limit=1000),
    lambda: reddit.subreddit('HurricaneHelene').hot(limit=1000),
    lambda: reddit.subreddit('HurricaneHelene').top(time_filter='month', limit=1000),
    lambda: reddit.subreddit('HurricaneHelene').rising(limit=1000)
]

for fetch_posts in filters:
    print(f"Processing posts from filter: {fetch_posts.__name__}")  # Print which filter is being processed
    try:
        for post in fetch_posts():
            print(f"Processing post: {post.title}")  # Print post title being processed

            # Process post title
            if contains_keyword(post.title, relevant_helene_keywords):
                sentiment = get_sentiment(post.title)
                titles_data.append({'Text': post.title, 'Sentiment': sentiment, 'Type': 'Title', 'Author': str(post.author)})
                print(f"Processed title sentiment: {sentiment}")  # Print sentiment for the title

            # Process post content (selftext)
            if contains_keyword(post.selftext, relevant_helene_keywords):
                sentiment = get_sentiment(post.selftext)
                posts_data.append({'Text': post.selftext, 'Sentiment': sentiment, 'Type': 'Content', 'Author': str(post.author)})
                print(f"Processed post content sentiment: {sentiment}")  # Print sentiment for the content

            # Process comments
            post.comments.replace_more(limit=0)
            for comment in post.comments.list():
                if contains_keyword(comment.body, relevant_helene_keywords):
                    sentiment = get_sentiment(comment.body)
                    comments_data.append({'Text': comment.body, 'Sentiment': sentiment, 'Type': 'Comment', 'Author': str(comment.author)})
                    print(f"Processed comment sentiment: {sentiment}")  # Print sentiment for the comment

            time.sleep(1)  # Respect Reddit's API rate limits
    except Exception as e:
        print(f"Error occurred: {e}")


# Save results to CSV
pd.DataFrame(titles_data).to_csv('filtered_helene_titles.csv', index=False)
pd.DataFrame(posts_data).to_csv('filtered_helene_posts.csv', index=False)
pd.DataFrame(comments_data).to_csv('filtered_helene_comments.csv', index=False)

print("Data saved successfully!")
