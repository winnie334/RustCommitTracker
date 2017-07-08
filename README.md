# RustCommitTracker

Are weekly updates not enough for you?

Do you want to stay up-to-date all the time?

Or do you simply want to be the first poster in /r/playrust, for that sweet sweet karma?

Look no further! RustCommitTracker notifies you any time a new commit is added.

![alt text](http://imgur.com/c5mticZ.gif "why are you reading this")

## Requirements

You must have Python 3 installed on a Windows 7, 8.1, 10 machine.

After Python has been installed, navigate to the project folder you just downloaded from this repository then
run the command **pip install -r requirements.txt** (you may have to run your command prompt as administrator)
and that'll get you squared away with all the requirements.

## Installation

Move the project folder into your C drive as such "C:\RustCommitTracker" or wherever you'd like, actually.

Right click and edit **install.bat** then change the first file path inside the string to your Python 3 installation folder.
Likely all you'll have to do is change **USERNAME** with your username and you'll be good to go.  

Don't know where Python is installed? Run **where python** in your command prompt.  

From here, go ahead and right click the **install.bat** and run as an administrator (since we're creating a task, this requires admin privileges).

Every time you log on you'll receive the latest commit that has been published and be notified of it regardless as to
how long ago the commit was actually made. So to finish up everything, log out of your account and log back in. You should see
a notification pop up with the most recent commit published!

This script will poll every 1 minute to check and see if there has been an update.