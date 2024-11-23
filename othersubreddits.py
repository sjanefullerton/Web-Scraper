import praw
import pandas as pd

# Define keywords for positive, negative, and neutral emotions
positive_emotions_keywords = [
    'happy', 'joyful', 'grateful', 'thankful', 'hopeful', 'relieved',
    'excited', 'optimistic', 'content', 'satisfied', 'peaceful',
    'cheerful', 'delighted', 'elated', 'inspired', 'confident',
    'proud', 'lucky', 'blessed', 'euphoric', 'joyous', 'appreciative',
    'calm', 'thankful', 'comfortable', 'grinning', 'smiling', 'motivated',
    'uplifted', 'refreshed', 'relaxed'
]
negative_emotions_keywords = [
    'sad', 'angry', 'frustrated', 'fearful', 'scared', 'hopeless', 'anxious',
    'depressed', 'disappointed', 'betrayed', 'guilty', 'hurt', 'nervous',
    'lonely', 'ashamed', 'heartbroken', 'desperate', 'grief', 'angst', 'upset',
    'devastated', 'terrified', 'dismayed', 'overwhelmed', 'despair',
    'miserable', 'distressed', 'shocked', 'helpless', 'vulnerable', 'isolated',
    'stressed', 'worried', 'frightened', 'discouraged', 'regretful', 'lost',
    'mental health', 'anxiety', 'depression', 'emotional distress'
]
neutral_emotions_keywords = [
    'neutral', 'indifferent', 'calm', 'bored', 'apathetic', 'indifferent',
    'detached', 'reserved', 'unmoved', 'unconcerned', 'unaffected',
    'unenthusiastic', 'unimpressed', 'moderate', 'nonchalant', 'passive',
    'unperturbed', 'balanced', 'steady', 'unexcited', 'uninvolved'
]

# Additional Keywords for matching posts (Hurricane Helene, Mental Health, Locations, etc.)
relevant_keywords = [
    'helene', 'hurricane helene', 'tropical storm helene', 'storm helene'
]

# Initialize the Reddit API client
reddit = praw.Reddit(
    client_id='R56d6atFieHcJoZqQDQQmQ',  # Replace with your client ID
    client_secret='NajuFmUCAu8FREQww0u__ag53_m0KA',  # Replace with your client secret
    user_agent='script:my_hurricane_scraper:v1.0 (by u/sjanesasha)'
)


# Function to check if a text contains any of the relevant sentiment keywords AND any of the Helene-related keywords (case insensitive)
def contains_keyword(text, sentiment_keywords, helene_keywords):
    text = text.lower()

    # Check if any sentiment-related keywords are in the text
    sentiment_match = any(keyword.lower() in text for keyword in sentiment_keywords)

    # Check if any Helene-related keywords are in the text
    helene_match = any(keyword.lower() in text for keyword in helene_keywords)

    # Return True if both conditions are met
    return sentiment_match and helene_match

# Function to determine the sentiment based on keywords (Positive, Negative, or Neutral)
def get_sentiment(text):
    if contains_keyword(text, positive_emotions_keywords):
        return 'Positive'
    elif contains_keyword(text, negative_emotions_keywords):
        return 'Negative'
    elif contains_keyword(text, neutral_emotions_keywords):
        return 'Neutral'
    else:
        return None  # If no sentiment keyword matches


# Create empty lists to hold the post and comment data
titles_data = []
posts_data = []
comments_data = []

# List of subreddits to scrape
subreddits = ['mentalhealth', 'MentalHealthSupport', 'depression', 'anxiety', 'florida', 'Georgia', 'NorthCarolina',
              'Tennessee', 'Virginia']

# Loop through each subreddit
for subreddit_name in subreddits:
    print(f"Scraping from subreddit: {subreddit_name}")
    posts = reddit.subreddit(subreddit_name).new(limit=100)  # Adjust the limit as needed

    # Loop through posts and extract relevant information
    for idx, post in enumerate(posts, start=1):
        try:
            # Print progress message
            print(f"Processing post {idx} from {subreddit_name}...")

            # Process the post title (Separate dataset for titles)
            sentiment_title = get_sentiment(post.title)
            if sentiment_title and contains_keyword(post.title, relevant_keywords):
                titles_data.append({
                    'Text': post.title,
                    'Sentiment': sentiment_title,
                    'Type': 'Title',
                    #'Post URL': post.url,
                    #'Created': post.created_utc,
                    #'Author': str(post.author),
                    'Subreddit': subreddit_name
                })

            # Process the post content (selftext) and add to posts dataset
            sentiment_content = get_sentiment(post.selftext)
            if sentiment_content and contains_keyword(post.selftext, relevant_keywords):
                posts_data.append({
                    'Text': post.selftext,
                    'Sentiment': sentiment_content,
                    'Type': 'Content',
                    #'Post URL': post.url,
                    #'Created': post.created_utc,
                    #'Author': str(post.author),
                    'Subreddit': subreddit_name
                })

            # Process the comments and add to comments dataset
            post.comments.replace_more(limit=0)  # Load all comments
            for comment in post.comments.list():
                sentiment_comment = get_sentiment(comment.body)
                if sentiment_comment and contains_keyword(comment.body, relevant_keywords):
                    comments_data.append({
                        'Text': comment.body,
                        'Sentiment': sentiment_comment,
                        'Type': 'Comment',
                        #'Post URL': post.url,
                        #'Created': post.created_utc,
                        #'Comment Author': str(comment.author),
                        'Subreddit': subreddit_name
                    })

        except Exception as e:
            print(f"Error occurred with post {idx} from {subreddit_name}: {e}")

# Convert the titles, posts, and comments data to Pandas DataFrames
titles_df = pd.DataFrame(titles_data)
posts_df = pd.DataFrame(posts_data)
comments_df = pd.DataFrame(comments_data)

# Save the data to CSV files
titles_df.to_csv('multi_subreddit_titles.csv', index=False)
posts_df.to_csv('multi_subreddit_posts.csv', index=False)
comments_df.to_csv('multi_subreddit_comments.csv', index=False)

print("Data saved to 'multi_subreddit_titles.csv', 'multi_subreddit_posts.csv', and 'multi_subreddit_comments.csv'")