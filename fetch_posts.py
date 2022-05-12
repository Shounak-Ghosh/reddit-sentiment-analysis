import requests
import pandas as pd
import reddit_oauth as auth


def subreddit_post_scraper(subreddit, category, limit):
    """
    Scrape posts from a subreddit
    @param subreddit: subreddit to scrape
    @param category: category of posts to scrape
    @param limit: number of posts to scrape
    """
    res = requests.get("https://oauth.reddit.com/r/{}/{}".format(subreddit, category),
                       headers=auth.headers)
    rows = [[post['data']['subreddit'],
             post['data']['title'],
             post['data']['selftext'],
             post['data']['upvote_ratio'],
             post['data']['ups'],
             post['data']['downs'],
             post['data']['score']] for post in res.json()['data']['children']]
    df = pd.DataFrame(rows, columns=[
                      'subreddit', 'title', 'selftext', 'upvote_ratio', 'ups', 'downs', 'score'])
    return df.head(limit)

print(subreddit_post_scraper('python', 'hot', 10))
print(subreddit_post_scraper('python', 'new', 10))