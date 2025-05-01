from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="sens.env")
username = os.getenv("username")
password = os.getenv("password")
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")

"""print(f"reddit_username: {username}")
print(f"reddit_password: {password}")
print(f"reddit_client_id: {client_id}")
print(f"reddit_client_secret: {client_secret}")"""