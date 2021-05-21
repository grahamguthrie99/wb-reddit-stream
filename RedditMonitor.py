import praw
import pika

class RedditMonitor:
    def __init__(self, universe, publisher, reddit_key, reddit_secret, reddit_user, reddit_password, subreddit):
        self.universe = universe
        self.publisher = publisher
        self.reddit_key = reddit_key
        self.reddit_secret = reddit_secret
        self.reddit_user = reddit_user
        self.reddit_password = reddit_password
        self.subreddit = subreddit
        self.api = self._create_connection()
        
    def _create_connection(self):
        return praw.Reddit(
            client_id=self.reddit_key,
            client_secret=self.reddit_secret,
            password=self.reddit_password,
            user_agent="testscript by u/ggunit1875",
            username=self.reddit_user)
    
    def constructMessage(self, word):
        print("{}".format(word))
        return word

    def publishToQueue(self, message): 
        self.publisher.publish(message)
    
    def process_submission(self, submission):
        for word in submission.body.split():
            if word in self.universe.asset_list:
                message = self.constructMessage(word)
                self.publishToQueue(message)
                
    def run(self):     
        subreddit = self.api.subreddit(self.subreddit)
        for submission in subreddit.stream.comments():
            self.process_submission(submission)
                  





    
