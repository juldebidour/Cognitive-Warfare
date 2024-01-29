from instapy import InstaPy
from instapy import smart_run
import time 
def run_instagram_bot(username, password, hashtags):
    session = InstaPy(username=username, password=password)

    with smart_run(session):
        # Set up your bot's actions here
        session.like_by_tags(hashtags, amount=5)
        time.sleep(10)  # Wait for 30 seconds before the next action
        
if __name__ == "__main__":
    username = 'jul_instabot'
    password = 'InstaBot'
    hashtags = ['#chocolate']

    run_instagram_bot(username, password, hashtags)