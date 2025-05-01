import praw
import config
import time
import os

def bot_login(): #Praw.reddit establishes a connection with reddits API. Once that happens, it returns the created instance so that we can use it to further instruct the reddit API in other parts of the code. 
    try:
        reddit = praw.Reddit(
            username=config.username,
            password=config.password,
            client_id=config.client_id,
            client_secret=config.client_secret,
            user_agencdt="v0.1"
        )
        print("Logged in successfully!")
        return reddit
    except Exception as e:
        print(f"An error occurred while logging in: {e}")
        return None

def fetch_top_posts(reddit):
    top_posts = []
    subreddits = ['gaming', 'science', 'technology', 'formula1', 'movies']
    for subreddit in subreddits: #for each of the subreddits in the list, append the top post of the day to the new list 
        for submission in reddit.subreddit(subreddit).top(time_filter = 'day', limit=1): #this is one of the primary commands to fetch info using PRAW from reddit. 
            top_posts.append(submission)
    return top_posts

def compile_digest(top_posts): #takes each of the top post, formats it then adds it to the digest string. 
    digest = "### In Today's Unimportant News\n\n"
    for i, post in enumerate(top_posts):
        digest += f"{i + 1}. **{post.title}**\n\n  Link: {post.url}\n\n"
    return digest

def post_digest(reddit, digest): #command to make a post in the test subreddit.
    reddit.subreddit('test').submit('Daily News Digest', selftext=digest)

def main(): #call all the functions. 
    reddit = bot_login()
    if reddit:
        top_posts = fetch_top_posts(reddit)
        digest = compile_digest(top_posts)
        post_digest(reddit, digest)
        print("Digest posted successfully!")

main()
