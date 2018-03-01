from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

consumer_key        = ''
consumer_secret     = ''
access_token        = ''
access_token_secret = ''

class listener(StreamListener):

    def __init__(self):
        self.dataDic = []

    def on_data(self, data):
        print("# " + str(self.dataDic.__len__()) + " Data:", data)
        objData = json.loads(data)
        self.dataDic.append(objData)
        return True

    def on_error(self, status):
        print("Error:", status)

    def get_data(self):
        return self.dataDic

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

twitterListener = listener()

try:
    twitterStream = Stream(auth, twitterListener)
    twitterStream.filter(track=["a"])
except:

    twitterStream.running = False
    print("exporting data")
    with open('data.json', 'w') as outfile:
        json.dump(twitterListener.get_data(), outfile)
    print("export data ok")
