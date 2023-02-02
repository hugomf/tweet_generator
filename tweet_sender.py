from sqs_sender import SQSSender
from tuit_bot import TuitBot
import time
from env_config import (
    TWITTER_USERNAME, 
    TWITTER_PASSWORD, 
    QUEUE_NAME
) 

def main():


    sqs = SQSSender(QUEUE_NAME)
    tweeter = TuitBot(False, TWITTER_USERNAME, TWITTER_PASSWORD)
    tweeter.login()

    while True:
        message = sqs.receive_message()
        if message is None:
            continue
        status = tweeter.post(message, 3)
        if status == "OK":
            sqs.remove_message()

        time.sleep(5)
    


if __name__ == '__main__':
    main()