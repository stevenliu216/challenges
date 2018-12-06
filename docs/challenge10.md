# Challenge 10
Write a class to retrieve tweets from the Twitter API
In this 3 part challenge you will analyze Twitter Data.
This week we will automate the retrieval of data. In Part 2 we will
task you with finding similar tweeters, and for Part 3 you will do a
full sentiment analysis.

- Define a class called UserTweets that takes a Twitter handle / user in its constructor. it also receives an optional max_id parameter to start from a particular tweet id.

- Create a tweepy API object using the tokens imported from config.py (again, you can use another package if you prefer).

- Create an instance variable to hold the last 100 tweets of the user.

- Implement len() and getitem() magic (dunder) methods to make the UserTweets object iterable.

- Save the generated data as CSV in the data subdirectory: data/some_handle.csv, columns: id_str,created_at,text


### Function prototype:
    from collections import namedtuple
    import csv
    import os

    import tweepy

    from .config import CONSUMER_KEY, CONSUMER_SECRET
    from .config import ACCESS_TOKEN, ACCESS_SECRET

    DEST_DIR = 'data'
    EXT = 'csv'
    NUM_TWEETS = 100

    Tweet = namedtuple('Tweet', 'id_str created_at text')


    class UserTweets(object):

        def __init__(self, handle, max_id=None):
            """Get handle and optional max_id.
            Use tweepy.OAuthHandler, set_access_token and tweepy.API
            to create api interface.
            Use _get_tweets() helper to get a list of tweets.
            Save the tweets as data/<handle>.csv"""
            # ...
            self._tweets = list(self._get_tweets())
            self._save_tweets()

        def _get_tweets(self):
            """Hint: use the user_timeline() method on the api you defined in init.
            See tweepy API reference: http://docs.tweepy.org/en/v3.7.0/api.html
            Use a list comprehension / generator to filter out fields
            id_str created_at text (optionally use namedtuple)"""
            pass

        def _save_tweets(self):
            """Use the csv module (csv.writer) to write out the tweets.
            If you use a namedtuple get the column names with Tweet._fields.
            Otherwise define them as: id_str created_at text
            You can use writerow for the header, writerows for the rows"""
            pass

        def __len__(self):
            pass

        def __getitem__(self, pos):
            pass


    if __name__ == "__main__":

        for handle in ('pybites', '_juliansequeira', 'bbelderbos'):
            print('--- {} ---'.format(handle))
            user = UserTweets(handle)
            for tw in user[:5]:
                print(tw)
            print()
 
### Example
##### Sample Input
    >>> from challenge10 import UserTweets
    >>> tweets = UserTweets('pybites')
    >>> len(tweets)
    100
    >>> tweets[0]
    Tweet(id_str='825629570992726017', created_at=datetime.datetime(2017, 1, 29, 9, 0, 3), text='Twitter digest 2017 week 04 https://t.co/L3njBuBats #python')
 
##### Sample Output
    $ head -3 data/pybites.csv
    id_str,created_at,text
    825629570992726017,2017-01-29 09:00:03,Twitter digest 2017 week 04 https://t.co/L3njBuBats #python
    825267189162733569,2017-01-28 09:00:05,Code Challenge 03 - PyBites blog tag analysis - Review https://t.co/xvcLQBbvup #python
 
### Explanation
The program gets the last 100 tweets and saves them to a handle_name.csv file
