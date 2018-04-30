"""
Simple twitter crawler program to gather Hungarian tweets
Authentication and twitter access

Author: Tim Day, Réka Juhász
Assignment 1, Statistical Natural Language Processing course
University of Tübingen, 2018
"""
import tweepy

auth = tweepy.OAuthHandler('ldZdf11vczxzyPcqVdXjbjKqF', '3dms2CXd7QnphABKx1jpTqw9kEiSLS82SWhBowdBvAFJPVRzKL')
auth.set_access_token('2312415672-jkPJ8x6CysNMkwxXvGjwAgntXsgisdHxMMWniBU', 'k755hrhZLHkes8KP7nqZfEtayCxOPCX8maJqXnSEa6A8m')

api = tweepy.API(auth, wait_on_rate_limit=True)

try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print('Error! Failed to get request token.')
