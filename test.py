import instaloader
from pprint import pprint

username = "boogywoogy2024"
password = "lockscreen"
target_username = "arman.singh.grewal"

L = instaloader.Instaloader()
L.login(username, password)
print(f"Logged in as {username}, loading information for {target_username}")

profile = instaloader.Profile.from_username(L.context, target_username)  
followers = {f.username for f in set(profile.get_followers())}
following = {f.username for f in set(profile.get_followees())}
not_following_back = following - followers
print("**"*30 + "\nFollowers:" + str(len(followers))); # pprint(followers)
print("**"*30 + "\nFollowing:" + str(len(following))); # pprint(following)
print("**"*30 + "\nNot Following Back:" + str(len(not_following_back))); # pprint(not_following_back)
import ipdb; ipdb.set_trace()
