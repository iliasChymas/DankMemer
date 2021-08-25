from typing_extensions import ParamSpecKwargs
import praw
import random
from praw.reddit import Subreddit
from dotenv import load_dotenv
import requests
import re
import os

load_dotenv(override=True)


reddit = praw.Reddit(
    client_id = os.getenv('client_id'),
    client_secret = os.getenv("client_secret"),
    password = os.getenv("password"),
    user_agent = "mae",
    username = os.getenv("username"),
    check_for_async=False)
print("Authed with reddit")

dark_subreddits = [ "dankmemes", "dankchristianmemes", "Memes_Of_The_Dank", "ComedyCemetery", "greececirclejerk", "HolUp", "NSFWFunny"]

def get_random_post(subreddit):
    posts = [post for post in subreddit.hot(limit=120) if post.url.split('.')[-1] in ['gif', 'jpg', 'png']]
    return random.choice(posts)

def get_hot(category):
    category = category.lower()
    subreddit = ''
    if category == 'blonde':
        subreddit = random.choice(["Blonde", "blondegirlsfucking"])
    elif category == "redhead":
        subreddit = random.choice(["redhead", "RedheadGifs", "redheadxxx"])
    elif category == "boobs":
        subreddit = random.choice(["boobs", "BoobsAndTities", "BoobsInAction"])
    elif category == "glasses":
        subreddit = random.choice(['glassesNSFW', "GlassesGoneWild"])
    elif category == "ass":
        subreddit = random.choice(['bigasses', "ass"])
    elif category == "milf":
        subreddit = random.choice(['HotMoms', "milf", "milfsdoporn", "Miflie"])
    elif category == "japanese":
        subreddit = random.choice(["japanpornstars", "NSFW_Japan", "JapanesePorn2"])
    elif category == 'porn':
        subreddit = random.choice(["nsfw", "porn", "NSFW_GIF", "HardcoreNSFW"])
   
    post = reddit.subreddit(subreddit).random()
    url = post.url
    if "redgifs" in post.url:  
        r = requests.get(post.url)
        link = re.search('"contentUrl":(.*).gif"', r.text)
        #print(r.text)
        url = link.group().replace('"contentUrl":', "").replace("\\", '', 4).replace('"', "", 2)
        print(url)
    
    return url, post.title
  

def download_meme():
    
    subr = reddit.subreddit(random.choice(dark_subreddits)) #get_random_post(reddit.subreddit(random.choice(dark_subreddits)))
    post = get_random_post(subr)
    #correct_post_list = [post for post in posts if post.url.split('.')[-1] in ["jpg", "png", "gif", "gifv"]]
    #p = random.choice(correct_post_list)
    return post.url, post.title

def get_pun():
    post = reddit.subreddit('dadjokes').random()
    return post.title, post.selftext

