import schedule
import time

import ml
from planning import Agenda

N_TWEETS_PER_DAY = 20
HOURS_ACTIVE_PR_DAY = 12
WAKEUP_TIME = "14:00"


def main():
    tweet_generator = ml.TweetGenerator()
    agenda = Agenda()

    def populate_agenda():
        agenda.schedule_random(
            action=tweet_generator.post_random_tweet(),
            timespan_hours=HOURS_ACTIVE_PR_DAY,
            n_events=N_TWEETS_PER_DAY)
        return

    schedule.every().day.at(WAKEUP_TIME).do(populate_agenda)
    schedule.every(1).minutes.do(agenda.run_due_tasks)

    while True:
        schedule.run_pending()
        time.sleep(10)
