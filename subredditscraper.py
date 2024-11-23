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
    'uplifted', 'refreshed', 'relaxed', 'good'
]
negative_emotions_keywords = [
    'sad', 'angry', 'frustrated', 'fearful', 'scared', 'hopeless', 'anxious',
    'depressed', 'disappointed', 'betrayed', 'guilty', 'hurt', 'nervous',
    'lonely', 'ashamed', 'heartbroken', 'desperate', 'grief', 'angst', 'upset',
    'devastated', 'terrified', 'dismayed', 'overwhelmed', 'despair',
    'miserable', 'distressed', 'shocked', 'helpless', 'vulnerable', 'isolated',
    'stressed', 'worried', 'frightened', 'discouraged', 'regretful', 'lost',
    'doom', 'bad'
]
# Neutral emotions/feelings keywords
neutral_emotions_keywords = [
    'neutral', 'indifferent', 'calm', 'bored', 'apathetic', 'indifferent',
    'detached', 'reserved', 'unmoved', 'unconcerned', 'unaffected',
    'unenthusiastic', 'unimpressed', 'moderate', 'nonchalant', 'passive',
    'unperturbed', 'balanced', 'steady', 'unexcited', 'uninvolved'
]

# Helene keywords
helene_keywords = [
    'helene', 'hurricane helene', 'tropical storm helene', 'storm helene',
    'hurricane', 'tropical storm', 'storm', 'cyclone', 'typhoon',
    'storm surge', 'storm damage', 'storm path', 'storm watch',
    'storm warning', 'tropical depression', 'weather event',
    'natural disaster', 'storm recovery', 'evacuation', 'evacuees',
    'first responders', 'category 1 hurricane', 'category 2 hurricane',
    'category 3 hurricane', 'category 4 hurricane', 'category 5 hurricane',
    'power outages', 'electricity down', 'blackout', 'damage', 'destruction',
    'flooding', 'flooded', 'landslide', 'debris', 'property damage',
    'fallen trees', 'downed power lines', 'power restoration', 'roof damage',
    'infrastructure damage', 'flooded roads', 'waterlogged', 'recovery efforts',
    'rescue efforts', 'relief efforts', 'recovery teams', 'search and rescue',
    'aid', 'shelter', 'temporary housing', 'mental health', 'trauma',
    'emotional impact', 'psychological effects', 'disaster relief',
    'storm track', 'hurricane models', 'storm warnings', 'hurricane center',
    'storm updates', 'wind speed', 'rainfall', 'precipitation', 'barometric pressure',
    'weather alerts', 'weather service', 'disaster', 'emergency', 'catastrophe',
    'crisis', 'evacuation order', 'emergency shelters', 'FEMA', 'Red Cross',
    'disaster recovery', 'hurricane damage', 'hurricane recovery', 'storm aftermath',
    'storm survivors', 'displaced people', 'Hurricane Helene aftermath', 'storm aftermath',
    'Hurricane Helene path', 'Hurricane Helene recovery', 'shelter locations',
    'evacuation orders', 'rescue teams', 'weather event', 'displaced residents'
]

# Initialize the Reddit API client
reddit = praw.Reddit(
    client_id='R56d6atFieHcJoZqQDQQmQ',  # Replace with your client ID
    client_secret='NajuFmUCAu8FREQww0u__ag53_m0KA',  # Replace with your client secret
    user_agent='script:my_hurricane_scraper:v1.0 (by u/sjanesasha)'
)

# Function to check if a text contains any of the relevant sentiment keywords AND any of the Helene-related keywords (case insensitive)
def contains_keyword(text):
    text = text.lower()

    # Check if any sentiment-related keywords are in the text
    sentiment_match_negative = any(keyword.lower() in text for keyword in negative_emotions_keywords)
    sentiment_match_positive = any(keyword.lower() in text for keyword in positive_emotions_keywords)
    sentiment_match_neutral = any(keyword.lower() in text for keyword in neutral_emotions_keywords)

    # Check if any Helene-related keywords are in the text
    helene_match = any(keyword.lower() in text for keyword in helene_keywords)

    # Return True if both conditions are met
    return (sentiment_match_negative | sentiment_match_positive | sentiment_match_neutral) and helene_match

# Function to determine the sentiment based on keywords (Positive, Negative, or Neutral)
def get_sentiment(text):
    if contains_keyword(text):
        if any(keyword.lower() in text for keyword in negative_emotions_keywords):
            return 'Negative'
        elif any(keyword.lower() in text for keyword in positive_emotions_keywords):
            return 'Positive'
        else:
            return 'Neutral'
    else:
        print("Did not match any sentiment keyword")

# Create empty lists to hold the post and comment data
titles_data = []
posts_data = []
comments_data = []

# Subreddits: ['mentalhealth', 'MentalHealthSupport', 'depression',
#               'anxiety', 'florida', 'Georgia', 'NorthCarolina',
#               'Tennessee', 'Virginia']

# Fetch posts from the subreddit
posts = reddit.subreddit('Virginia').new(limit=100)  # Adjust the limit as needed

# Loop through posts and extract relevant information
for post in posts:
    try:
        # Print progress message
        print(f"Processing post...")

        # Process the post title
        if contains_keyword(post.title):
            sentiment_title = get_sentiment(post.title)
            titles_data.append({
                'Text': post.title,
                'Sentiment': sentiment_title,
                'Type': 'Title',
                'Author': str(post.author)
            })

        # Process the post content (selftext) and add to posts dataset
        if contains_keyword(post.selftext):
            sentiment_content = get_sentiment(post.selftext)
            posts_data.append({
                'Text': post.selftext,
                'Sentiment': sentiment_content,
                'Type': 'Content',
                'Author': str(post.author)
            })

        # Process the comments and add to comments dataset
        post.comments.replace_more(limit=0)  # Load all comments
        for comment in post.comments.list():
            if contains_keyword(comment.body):
                sentiment_comment = get_sentiment(comment.body)
                comments_data.append({
                    'Text': comment.body,
                    'Sentiment': sentiment_comment,
                    'Type': 'Comment',
                    'Post URL': post.url,
                    'Created': post.created_utc,
                    'Comment Author': str(comment.author)
                })
    except Exception as e:
        print(f"Error occurred: {e}")

# Convert the titles, posts, and comments data to Pandas DataFrames
titles_df = pd.DataFrame(titles_data)
posts_df = pd.DataFrame(posts_data)
comments_df = pd.DataFrame(comments_data)

# Save the data to CSV files, change to subreddit being scraped
titles_df.to_csv('Virginia_titles.csv', index=False)
posts_df.to_csv('Virginia_posts.csv', index=False)
comments_df.to_csv('Virginia_comments.csv', index=False)

print("Data saved to 'subreddit_titles.csv', 'subreddit_posts.csv', and 'subreddit_comments.csv'")
