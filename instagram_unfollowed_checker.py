########################################## Change this Metadata ##########################################
# Enter the username and password of your own account
username = ""
password = ""
# Enter the target username whose unfollowers you want to check
target_username = ""
# Add the usernames of meme-pages your follow, They can be exempted from "not_following_back" list)
meme_pages_I_follow = {}

########################################## Main script ##########################################
import instaloader
import time
from pprint import pprint

print(f"\n------------------------ Starting:[{time.strftime('%Y-%m-%d %H:%M:%S')}] ------------------------")
L = instaloader.Instaloader()
L.login(username, password)
print(f"\nLogged in as {username}, loading information for {target_username}")

profile = instaloader.Profile.from_username(L.context, target_username)  
followers = {f.username for f in set(profile.get_followers())}
following = {f.username for f in set(profile.get_followees())}
not_following_back = following - (followers | meme_pages_I_follow)

print(f"\nFollowers: {len(followers)}")
print(f"Following: {len(following)}")
print(f"Not Following Back: {len(not_following_back)}")
# pprint(not_following_back) # Uncomment to print the names of 🐍

print(f"\n------------------------ Ending:[{time.strftime('%Y-%m-%d %H:%M:%S')}] ------------------------")
