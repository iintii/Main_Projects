<!-- 
  Replace the image link below with your own banner or an image you like!
  For example, you can upload one to Imgur and link it here.
-->
# 🤖 Reddit Daily News Digest Bot

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?style=flat-square&logo=python" alt="Python 3.10"/>
  <img src="https://img.shields.io/badge/PRAW-v7.x-green?style=flat-square" alt="PRAW"/>
  <img src="https://img.shields.io/badge/API-Reddit-important?style=flat-square" alt="Reddit API"/>
</p>

<p align="center">
  <b>A Reddit bot that logs in with stored credentials, fetches top posts from select subreddits, compiles them into a daily digest, and posts the digest to a subreddit.</b>
</p>

---

## 🚀 Overview

**Reddit Daily News Digest Bot** is a simple yet powerful project utilizing Reddit's API via [PRAW](https://praw.readthedocs.io/) and environment-based configuration with [python-dotenv](https://pypi.org/project/python-dotenv/). It:

- Loads API credentials from an environment file.
- Logs into Reddit using PRAW.
- Fetches the top daily post from selected subreddits (e.g., `gaming`, `science`, `technology`, `formula1`, `movies`).
- Compiles these posts into a formatted digest.
- Posts the digest to a target subreddit (currently set to `test`).

---

## ⚙️ How It Works

1. **Configuration Loading**  
   The project uses `python-dotenv` to read environment variables from a file (e.g., `sens.env`). This file stores sensitive data like `username`, `password`, `client_id`, and `client_secret`.

2. **Bot Login**  
   Using PRAW, the `bot_login()` function establishes a connection with Reddit's API. If successful, it returns a Reddit instance for further interactions.

3. **Fetching Top Posts**  
   The `fetch_top_posts(reddit)` function iterates over a given list of subreddits, fetching the top post of the day from each.

4. **Digest Compilation**  
   The `compile_digest(top_posts)` function formats the fetched submissions into a Markdown digest, including titles and links.

5. **Posting the Digest**  
   Finally, the `post_digest(reddit, digest)` function submits the digest as a post to a designated subreddit.

6. **Orchestration**  
   The `main()` function ties together these steps, ensuring that once logged in, the bot compiles and posts the daily digest.

---

## 🏗️ Project Structure

```plaintext
.
├── config.py          # Loads environment variables from sens.env using python-dotenv
├── main.py            # Contains the bot logic: login, fetch top posts, compile and post digest
├── sens.env           # Environment file storing Reddit API credentials (see below)
└── README.md          # This file
```
## ✅ Conclusion

Thank you for exploring this project!
