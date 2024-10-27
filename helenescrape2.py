import praw
import pandas as pd
import time

# Initialize the Reddit API client
reddit = praw.Reddit(
    client_id='',  # Replace with your client ID
    client_secret='',  # Replace with your client secret
    user_agent='script:my_hurricane_scraper:v1.0 (by u/sjanesasha)'
)


def fetch_posts(reddit_subreddit, search_term, date_limit, max_posts):
    post_data = []  # Rename to avoid shadowing
    post_count = 0
    after_post_id = None

    while post_count < max_posts:
        # Search for posts related to the specified term
        posts = reddit_subreddit.search(search_term, sort='new', limit=100, params={'after': after_post_id})

        # Convert ListingGenerator to list
        posts_list = list(posts)  # Convert to a list to allow indexing

        # Break if there are no posts found
        if not posts_list:
            break

        for post in posts_list:
            if post.created_utc >= date_limit:  # Use the new name here
                post_info = {
                    'Title': post.title,
                    'Post Content': post.selftext,
                    'URL': post.url,
                    'Score': post.score,
                    'Created': post.created_utc,
                    'Author': str(post.author),
                    'Subreddit': str(post.subreddit)
                }

                # Fetch comments for the post
                post.comments.replace_more(limit=0)
                comments = []
                for comment in post.comments.list():
                    comments.append({
                        'Comment Author': str(comment.author),
                        'Comment Body': comment.body
                    })

                post_info['Comments'] = comments
                post_data.append(post_info)  # Renamed to avoid shadowing
                post_count += 1

                # Break if we've reached the desired number of posts
                if post_count >= max_posts:
                    break

        # Update after_post_id to fetch the next set of results
        after_post_id = posts_list[-1].name if posts_list else None  # Change here to use posts_list
        if not after_post_id:
            break  # Break the loop if there are no more posts to fetch

    return post_data


# Define the date threshold (September 23, 2024)
date_threshold = int(time.mktime(time.strptime('2024-09-23', '%Y-%m-%d')))

# Fetch posts from Reddit
subreddit_instance = reddit.subreddit('all')  # Rename to avoid shadowing
data = fetch_posts(subreddit_instance, 'Hurricane Helene', date_threshold, max_posts=1000)

# Create a DataFrame from the collected data
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('hurricane_helene_posts2.csv', index=False)

print("Data saved to hurricane_helene_posts2.csv")
