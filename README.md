# Basic Working and thought process

We have a single script: `instagram_unfollowed_checker` which runs locally (A cronjob is set for this).
We also have a log file: `main.log` for tracking who unfollowed us!

The python script does all the big lifting. Here is a summary of the work it does:

* Checks if internet is available or not, if not then halt all further processes and add an entry to our log file notifying us that today's run was unsuccessfull due to internet problems
* Use `instaloader` module to find all *followers*, *following* and calculate *not_following_back* (taking care of the meme pages I follow)
* I am using a test account **boogywoogy2024** to be used as a bot🤖 to check who unfollowed me on my original account **arman.singh.grewal**
* This is the crontab: `0 12 * * * python3 /Users/armangrewal/Desktop/Research/InstaBOT/WhoTF_UnfollowedMe/instagram_unfollowed_checker.py`