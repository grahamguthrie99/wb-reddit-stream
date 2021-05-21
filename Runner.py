import os
from dotenv import load_dotenv
from Universe import Universe
from Publisher import Publisher
from RedditMonitor import RedditMonitor

def main():
    load_dotenv()
    universe = Universe(
        os.environ["ALPACA_CLIENT_ID"],
        os.environ["ALPACA_CLIENT_SECRET"],
        os.environ["ALPACA_ENDPOINT"]
    )

    publisher = Publisher(
        os.environ["HOST"], 
        os.environ["PORT"], 
        os.environ["EXCHANGE"], 
        os.environ["ROUTING_KEY"]
    )

    monitor = RedditMonitor(
        universe, 
        publisher,
        os.environ["REDDIT_KEY"],
        os.environ["REDDIT_SECRET"],
        os.environ["REDDIT_USER"],
        os.environ["REDDIT_PASSWORD"],
        os.environ["SUBREDDIT"]
    )
    monitor.run()

if __name__ == "__main__":
    main()