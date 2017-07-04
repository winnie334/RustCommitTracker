from notifier import balloon_tip
from bs4 import BeautifulSoup
import requests, time, datetime, calendar


class Commit:
	def __init__(self, author, text, number):
		self.author = author
		self.text = text
		self.number = number


def getcommits(url):		# returns a list of classes, each class represents a commit.
	source = requests.get(url)
	soup = BeautifulSoup(source.text, "html.parser")
	commits = soup.find_all('div', {'class': 'media-content'})
	commitlist = []
	for commit in commits:
		author = commit.find('small').text
		text = commit.find('div', {'class': 'pre'}).text.split('\n')
		number = int(commit.find('a')['href'][1:])
		for line in text:
			c = Commit(author, line, number)
			commitlist.append(c)
	return commitlist

if __name__ == '__main__':
	timeout = 300		# time in seconds it needs to wait between every check (higher == later notifications)
	show_private = 0		# if this is 1, it will also notify you of commits with the text shown below
	private = "This commit has been marked as private, so it is hidden"
	icon = "rusticon.ico"
	rclass = balloon_tip("I'm starting!", "Let's hope the commits will be plenty!", icon)		# subtly define rclass
	now = datetime.datetime.now()		# the url changes every month, joy oh joy
	url = "https://rust.facepunch.com/commits/" + str(now.year) + "/" + calendar.month_name[now.month]
	currentnumber = getcommits(url)[0].number		# get the number of the latest commit to start comparing new ones with
	while True:
		time.sleep(timeout)
		commitlist = getcommits(url)
		if commitlist[0].number > currentnumber:
			amount = commitlist[0].number - currentnumber
			for i in range(amount):
				if private == commitlist[i].text and show_private == 0:
					pass
				else:
					title = commitlist[i].author + " [#" + str(commitlist[i].number) + "]"
					balloon_tip(title, commitlist[i].text, icon, rclass)
			currentnumber = commitlist[0].number
