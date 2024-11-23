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

# Function to check if a text contains any of the relevant keywords (case insensitive)
def contains_keyword(text, keywords):
    text = text.lower()
    return any(keyword.lower() in text for keyword in keywords)

# Function to determine the sentiment based on keywords (Positive, Negative, or Neutral)
def get_sentiment(text):
    if contains_keyword(text, negative_emotions_keywords):
        return 'Negative'
    elif contains_keyword(text, positive_emotions_keywords):
        return 'Positive'
    else:
        return 'Neutral'

# Create empty lists to hold the post and comment data
titles_data = []
posts_data = []
comments_data = []

# Fetch posts from the 'HurricaneHelene' subreddit
posts = reddit.subreddit('HurricaneHelene').new(limit=3000)  # Adjust the limit as needed

# Loop through posts and extract relevant information
for post in posts:
    try:
        # Print progress message
        print(f"Processing post...")

        # Process the post title
        if contains_keyword(post.title, relevant_helene_keywords):
            sentiment_title = get_sentiment(post.title)
            titles_data.append({
                'Text': post.title,
                'Sentiment': sentiment_title,
                'Type': 'Title',
                #'Post URL': post.url,
                #'Created': post.created_utc,
                'Author': str(post.author)
            })

        # Process the post content (selftext) and add to posts dataset
        if contains_keyword(post.selftext, relevant_helene_keywords):
            sentiment_content = get_sentiment(post.selftext)
            posts_data.append({
                'Text': post.selftext,
                'Sentiment': sentiment_content,
                'Type': 'Content',
                #'Post URL': post.url,
                #'Created': post.created_utc,
                'Author': str(post.author)
            })

        # Process the comments and add to comments dataset
        post.comments.replace_more(limit=0)  # Load all comments
        for comment in post.comments.list():
            if contains_keyword(comment.body, relevant_helene_keywords):
                sentiment_comment = get_sentiment(comment.body)
                comments_data.append({
                    'Text': comment.body,
                    'Sentiment': sentiment_comment,
                    'Type': 'Comment',
                    'Post URL': post.url,
                    'Created': post.created_utc,
                    'Comment Author': str(comment.author)
                })
        time.sleep(2) # Add a delay between requests to avoid hitting Reddit's rate limit
    except Exception as e:
        print(f"Error occurred: {e}")

# Convert the titles, posts, and comments data to Pandas DataFrames
titles_df = pd.DataFrame(titles_data)
posts_df = pd.DataFrame(posts_data)
comments_df = pd.DataFrame(comments_data)

# Save the data to CSV files
titles_df.to_csv('3000_helene_titles.csv', index=False)
posts_df.to_csv('3000_helene_posts.csv', index=False)
comments_df.to_csv('3000_helene_comments.csv', index=False)

print("Data saved to '3000_helene_titles.csv', '3000_helene_posts.csv', and '3000_helene_comments.csv'")
