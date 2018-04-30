todo
- properly formatted docstrings in the program and the documentation. [Link](https://www.python.org/dev/peps/pep-0257/) to standards used for docstrings
- "Write another program that reads the corpus, and outputs only
the Tweet IDs.7 Your output should be a text file with a single tweet id per line"
... we did this all in one function. Break it out into 2. Test the new one on the hun.json file
(this step is probably to make us run into the problem of incorrectly formatted json, which we have already fixed so it should be a simple for loop)
- clean up the README file

# Assignment 1: creating a Twitter corpus
```
Simple twitter crawler program to gather Hungarian tweets

Author: Tim Day, Réka Juhász
Assignment 1, Statistical Natural Language Processing course
University of Tübingen, 2018
```

In this assignment you will collect a corpus from Twitter.
Please see the [assignment sheet](https://snlp2018.github.io/assignment1.pdf) for details.

## Document your approach (Exercise 4)
Our language is Hungarian

### Language Collection Method
We first used tweepy geocode to restrict the physical location of tweets to the city of Budapest.
We then used twitters in-built language detection to filter for tweets tagged as Hungarian.

We tried the langdetect library, but it was having issues with tweets 'with no features' and crashing the program.
Presumably these were bots tweeting URLs or something like that.
The twitter tags were providing good results, so we just went with that method rather than tinkering with langdetect.

### Resources Used
tweepy - python wrapper for twitter API
json python library
twitter
twitter dev application management


### Yield Rate

The yield rate for the final trial that produced our corpus was as follows:

running yield rate:  0.8435970980259828
tweets so far /10000 10000

all other test trials wer within ~0.005 of this number


### Detailed Notes
- pip install tweepy [docs](http://docs.tweepy.org/en/v3.6.0/cursor_tutorial.html) and import it to python project
- create twitter account
- go to [twitter application management](https://apps.twitter.com/), create new twitter application
- obtain consumer keys and access tokens for use in python app (these are not shared on github)

In Python
- import json, for use when creating the output json file
- Use the tweepy.Cursor object to:
	- gather tweets by geolocation using the geocode parameter. We restricted to tweets from the city of Budapest
	- do not truncate tweets > 140 characters, by using the extended text parameter
	- use twitters language detection (available in the tweet metadata), by using the lang parameter
	
- In a separate function, we filtered the tweets for length (at least 50 characters)
- only those tweets that had enough characters were appended to to the json file, or had their id added to the hun.id file
- we took a large sample of tweets with tweepy.Cursor, and then used a counter in a for loop to stop the program when we had 10,000 tweets that met our filter criteria
- to ensure the the json was formatted correctly (ie with only one root node), we first created a node with an array in it, and appended the json data for each qualified tweet as an item in that array.

note: the json file data is stored on one line. You can use a [formatter](https://jsonformatter.curiousconcept.com/) for easier reading
note: we were able to inspect the twitter json output format using the twitter [docs](https://developer.twitter.com/en/docs/tweets/tweet-updates)


- RUNTIME BUG SQUASH we an issue with langdetect: langdetect.lang_detect_exception.LangDetectException: No features in text.
it seems that some tweets didn't have enough features for identification with this tool, and stopped the program during runtime. 
We remedied this by using the in-built twitter language classification, in the json tweet meta databy including the lang="hu" argument in the tweepy.Cursor object.
We could have probably persisted with the langdetect tool and tweaked the config, but the results we were getting from the twitter language identifier looked good.

- RUNTIME BUG SQUASH: tweepy.error.TweepError: Twitter error response: status code = 429
This had to do with twitters rate limits. After calling the API a certain number of times, a user is given a 15min timeout. 
This is presumably to decrease bot activity. We remedied it by adding "wait\_on\_rate_limit=True"" to the tweepy.API call

