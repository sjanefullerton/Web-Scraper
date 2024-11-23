import praw
import pandas as pd
import time

# Initialize the Reddit API client
reddit = praw.Reddit(
    client_id='R56d6atFieHcJoZqQDQQmQ',  # Replace with your client ID
    client_secret='NajuFmUCAu8FREQww0u__ag53_m0KA',  # Replace with your client secret
    user_agent='script:my_hurricane_scraper:v1.0 (by u/sjanesasha)'
)

# Search for posts related to "Hurricane Helene" in the 'anxiety' subreddit
posts_anxious = reddit.subreddit('HurricaneHelene').search('anxious', sort='relevance', limit=None)
posts_sad = reddit.subreddit('HurricaneHelene').search('sad', sort='relevance', limit=None)
posts_scared = reddit.subreddit('HurricaneHelene').search('scared', sort='relevance', limit=None)

# Define keywords that indicate relevance to Hurricane Helene
relevant_keywords = ['helene', 'storm helene', 'evacuate', 'evacuation', 'aftermath', 'damage', 'tropical storm', 'destruction', 'damage', 'power outages', 'debris', 'power lines down', 'recovery', 'rescue', 'relief', 'hurricane helene', 'sad', 'anxious', 'scared', 'impact', 'effects', 'recovery', 'mental health', 'experience', 'help', 'community', 'support']

# Function to check if the post is relevant
def is_relevant(post_title, post_content, comments):
    # Check title
    if any(keyword in post_title.lower() for keyword in relevant_keywords):
        return True
    # Check post content
    if any(keyword in post_content.lower() for keyword in relevant_keywords):
        return True
    # Check comments
    for comment in comments:
        if any(keyword in comment['Comment Body'].lower() for keyword in relevant_keywords):
            return True
    return False

# Create an empty list to store the data
data = []

# Iterate through the results and collect relevant information
for post in posts:
    try:
        post_info = {
            'Title': post.title,
            'Post Content': post.selftext,
            'URL': post.url,
            'Created': post.created_utc,
            'Author': str(post.author),
            'Subreddit': str(post.subreddit)
        }

        # Optionally fetch comments
        post.comments.replace_more(limit=0)
        comments = []
        for comment in post.comments.list():
            comments.append({
                'Comment Author': str(comment.author),
                'Comment Body': comment.body
            })

        post_info['Comments'] = comments

        # Check if the post is relevant before adding to the data
        if is_relevant(post_info['Title'], post_info['Post Content'], comments):
            data.append(post_info)

        # Add a delay to avoid hitting rate limits
        time.sleep(1)

    except Exception as e:
        print(f"An error occurred with post {post.title}: {e}")

# Create a DataFrame from the collected data
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('mayberelevant_hurricane_helene.csv', index=False)

print("Data saved to mayberelevant_hurricane_helene.csv")
