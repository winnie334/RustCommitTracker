# RustCommitTracker

Are weekly updates not enough for you?

Do you want to stay up-to-date all the time?

Or do you simply want to be the first poster in /r/playrust, for that sweet sweet karma?

Look no further! RustCommitTracker notifies you any time a new commit is added.

![alt text](http://imgur.com/c5mticZ.gif "why are you reading this")

## Requirements

You must have Python 2.7 installed on a Windows 7, 8.1, 10 machine. (linux support will be implemented shortly)
in order for the script to work it will need to be installed in "C:\Python27"

After Python has been installed, navigate to the project folder you just downloaded from this repository and
run the command "pip install -r requirements.txt" and that'll get you squared away with all the requirements.

## Installation

Move the project folder into your C drive as such "C:\RustCommitTracker"

Navigate inside the folder you just moved, and double click the "install.bat" file. This will create a task that's
scheduled to start the commit tracker whenever you log on to your computer. So for it to start up after installing you
will need to log off and log back on.

Every time you log on you'll receive the latest commit that has been published and be notified of it regardless as to
how long ago the commit was actually made.

This script will poll every 1 minute to check and see if there has been an update.