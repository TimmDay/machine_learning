"""
Simple twitter crawler program to gather Hungarian tweets
Authentication and twitter access
"""
import tweepy

auth = tweepy.OAuthHandler('#####', '#####')
auth.set_access_token('#-###', '#####')

api = tweepy.API(auth, wait_on_rate_limit=True)

try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print('Error! Failed to get request token.')
