import praw
import pandas as pd
import time

# Initialize the Reddit API client
reddit = praw.Reddit(
    client_id='',  # Replace with your client ID
    client_secret='',  # Replace with your client secret
    user_agent='script:my_hurricane_scraper:v1.0 (by u/sjanesasha)'
)
# Define the date threshold (September 23, 2024)
date_threshold = int(time.mktime(time.strptime('2024-09-23', '%Y-%m-%d')))

# Search for posts related to "Hurricane Helene"
subreddit = reddit.subreddit('all')
posts = subreddit.search('Hurricane Helene', sort='new', limit=1000)

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

        # Fetch the comments for the post
        post.comments.replace_more(limit=0)
        comments = []
        for comment in post.comments.list():
            comments.append({
                'Comment Author': str(comment.author),
                'Comment Body': comment.body
            })

        post_info['Comments'] = comments
        data.append(post_info)

    except Exception as e:
        print(f"An error occurred: {e}")

# Create a DataFrame from the collected data
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('hurricane_helene_posts1.csv', index=False)

print("Data saved to hurricane_helene_posts1.csv")
