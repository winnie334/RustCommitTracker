from notifier import balloon_tip
import time
import feedparser


class Tracker(object):
    def __init__(self):
        self.URL = "https://rust.facepunch.com/rss/commits/"
        self.commit_feed = feedparser.parse(self.URL)
        self.modified = self.commit_feed.modified
        self.commit = 0

    def update(self):
        feed = feedparser.parse(self.URL)
        current = feed.entries[0]
        if self.commit < int(current.title.split('/')[-1]):
            self.commit = int(current.title.split('/')[-1])
            balloon_tip(current.title, current.description)

    def fetch_update(self):
        feed = feedparser.parse(self.URL, modified=self.modified)
        if feed.status == 304:
            return
        self.update()

if __name__ == '__main__':
    tracker = Tracker()
    tracker.update()
    while True:
        tracker.fetch_update()
        time.sleep(60)
