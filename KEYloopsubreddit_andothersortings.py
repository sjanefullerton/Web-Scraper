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
    'uplifted', 'refreshed', 'relaxed', 'good', 'glad', 'heal', 'peace',
    'relief', 'hope'
]
negative_emotions_keywords = [
    'sad', 'angry', 'frustrated', 'fearful', 'scared', 'hopeless', 'anxious',
    'depressed', 'disappointed', 'betrayed', 'guilty', 'hurt', 'nervous',
    'lonely', 'ashamed', 'heartbroken', 'desperate', 'grief', 'angst', 'upset',
    'devastated', 'terrified', 'dismayed', 'overwhelmed', 'despair',
    'miserable', 'distressed', 'shocked', 'helpless', 'vulnerable', 'isolated',
    'stressed', 'worried', 'frightened', 'discouraged', 'regretful', 'lost',
    'doom', 'bad', 'hate', 'nightmare', 'overwhelmed', 'trauma', 'horrible',
    'regret', 'regrets', 'die', 'heartbreaking', 'heartbreak', 'overwhelming',
    'empty', 'struggle', 'afraid', 'pointless'
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
    return (sentiment_match_negative or sentiment_match_positive or sentiment_match_neutral) and helene_match

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
        return 'No relevant keywords found'

# Create empty lists to hold the post and comment data
titles_data = []
posts_data = []
comments_data = []

#subreddits = ['mentalhealth', 'MentalHealthSupport', 'depression',
               #'anxiety', 'florida', 'Georgia', 'NorthCarolina',
               #'Tennessee', 'Virginia']

subreddits = ['depression', 'NorthCarolina', 'Tennessee', 'Virginia']

for subreddit in subreddits:
    print(f"Scraping subreddit: {subreddit}")

    # Fetch posts: mix search, top, and new
    keywords = "mental health OR anxiety OR depression"
    filters = [
        #lambda: reddit.subreddit(subreddit).new(limit=100),
        lambda: reddit.subreddit(subreddit).top(time_filter="week", limit=100),
        lambda: reddit.subreddit(subreddit).search(keywords, sort="relevance", time_filter="month", limit=100)
    ]

    for filter_fn in filters:
        try:
            posts = filter_fn()

            for post in posts:
                # Process post titles
                if contains_keyword(post.title):
                    sentiment_title = get_sentiment(post.title)
                    titles_data.append({
                        'Text': post.title,
                        'Sentiment': sentiment_title,
                        'Type': 'Title',
                        'Author': str(post.author)
                    })

                # Process post content
                if contains_keyword(post.selftext):
                    sentiment_content = get_sentiment(post.selftext)
                    posts_data.append({
                        'Text': post.selftext,
                        'Sentiment': sentiment_content,
                        'Type': 'Content',
                        'Author': str(post.author)
                    })

                # Process comments
                post.comments.replace_more(limit=0)
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

                #time.sleep(1)

        except Exception as e:
            print(f"Error while processing subreddit {subreddit}: {e}")

    #time.sleep(2)


# Convert the lists to DataFrames
titles_df = pd.DataFrame(titles_data)
posts_df = pd.DataFrame(posts_data)
comments_df = pd.DataFrame(comments_data)

# Save the data to CSV files
titles_df.to_csv('3loop_titles.csv', index=False)
posts_df.to_csv('3loop_posts.csv', index=False)
comments_df.to_csv('3loop_comments.csv', index=False)

print("Data saved to '3loop_titles.csv', '3loop_posts.csv', and '3loop_comments.csv'")
