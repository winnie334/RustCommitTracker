# RustCommitTracker

Are weekly updates not enough for you?

Do you want to stay up-to-date all the time?

Or do you simply want to be the first poster in /r/playrust, for that sweet sweet karma?

Look no further! RustCommitTracker notifies you any time a new commit is added.

![alt text](http://imgur.com/c5mticZ.gif "why are you reading this")

## Installation

*Note beforehand: this is the first time I'm doing this, so if you notice anything that could be improved, please tell me!*

First off, download all these files and put them in a folder somewhere.

Now, right click on the batch file and press 'edit'. Replace *C:\Users\winnie33\PycharmProjects\RustCommitTracker\RustCommitTracker.py* with the path to your .py file. This batch file will execute the program with pythonw, so it runs in the background without disturbing you.

After that, edit the .vbs file and change the path once again. Note that you must now insert the path to the **.bat file**, not the .py file. This Visual Basic Script will be executed when starting your computer. The reason we don't simply execute the .bat file is to prevent a window popping up each time we start our computer.

To make this script run on startup, open a Run dialog box (Windows key + R) and type in the following:

*shell:startup*
  
Press enter and you'll see a folder appear. Cut and paste the .vbs file here. It will now execute each time on startup.

That's it! You're now good to go.

## Parameters

There are a few parameters you can adjust to make the program more enjoyable. They can be found in the RustCommitTracker.py file itself, on lines 27 and 28. There's probably a better way to do this, but this'll do just fine.

  * Timeout

   This is the delay between each request to the Rust website. It's given in seconds, and defaults to 300 (5 minutes). Lowering this number will notify you even sooner of a new commit, but may be intensive for your internet.
  
  * Show private commits
  
  Sometimes a commit is marked private and will thus not show its text. If you want you can still be notified of these commits. Changing show_private to 1 will make the program notify you of every single new commit. Defaults to 0.
  
## Afterword

This is my first time writing a program meant for distribution, so please forgive me for any mistakes. I definitely have the feeling I missed some important things, so if you could let me know it would be highly appreciated. Any improvements are of course welcome as well. Thanks for reading this and have a good day!
