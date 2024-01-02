########################################## Change this Metadata ##########################################
username = "boogywoogy2024"
password = "lockscreen"
target_username = "arman.singh.grewal"

meme_pages_I_follow = {'420iqhumor.in', '420iqhumour', 'apexwealthbuilder', 'beast.guy_93', 
                       'brampton_khaas', 'camjaraad', 'canadaconfession', 'chemicalburnol',
                       'cistheta.page', 'cybernikunj', 'datascience__expert', 'deepdarknowledge',
                       'disruptdetective', 'dscvrm', 'earlofdadjokes', 'electricpants', 
                       'explosmofficial', 'ezsnippet', 'fuddu_gallan', 'iammunnakmemes10', 
                       'ibengaluru', 'imjoblessguy', 'india.in.pixels', 'indianarmy.adgpi', 
                       'leomessi','lifeandscarz','log.kya.kahenge','luxx.ded','machinelearning',
                       'makeupartistbyridhimak','marketing.fanatic','mathematicsforlife','mutant1643',
                       'offical_boota_kaleke','perpendicular_radar','prashant.edits','print.floyd',
                       'producerdxx','project.jdm','punjabi_binnu','pycoders','retropunjabi','sadde_ale',
                       'sarcastic_us','scireviews','scoopwhoop','scse_lpu','seep_aala','showerfeelings',
                       'slimjim','strictlychamkila','studiesinfacts','surroorgasm','tao_philosophy',
                       'techacks__','theindiansarcasm','themanakchannel','technical_sapien','time4knowledge',
                       'we_all_love_coding_interviews','zoodraws_comic'}

some_people_more_famous_than_me = {'cristiano', 'davidlaid', 'drsukhpreetsinghudhoke', 'karanaujla_official', 
                                   'kashishggupta', 'okaybhullar','rishfits', 'sidhu_moosewala', 'trainwithrc'}

some_mfs_I_forgive = {'baba_nanak.1313', 'coachkhanna', 'vector_0g', 'newlook_sloon', 
                      'taatva_boy', 'tanyasrivastava251', 'tightest_upper_bound'}

to_be_exempted = meme_pages_I_follow | some_people_more_famous_than_me | some_mfs_I_forgive

############################################### Imports ###################################################

import socket
import time
import instaloader
from pprint import pprint

def is_internet_available():
    try:
        # Attempt to resolve a hostname to verify internet connectivity
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        # Log the absence of an internet connection to a logfile (creates if not exists)
        with open('main.log', 'a') as file:
            file.write(f"\n[{time.strftime('%Y-%m-%d %H:%M:%S')}] --> No internet connection detected.\n")
        return False  

############################################### Logging in ###############################################
if is_internet_available():
    file = open("main.log", "a")
    file.write(f"\n------------------------ Starting:[{time.strftime('%Y-%m-%d %H:%M:%S')}] ------------------------")
    L = instaloader.Instaloader()
    L.login(username, password)
    file.write(f"\nLogged in as {username}, loading information for {target_username}")

    profile = instaloader.Profile.from_username(L.context, target_username)  
    followers = {f.username for f in set(profile.get_followers())}
    following = {f.username for f in set(profile.get_followees())}
    not_following_back = following - (followers | to_be_exempted)

    # If some mf has unfollowed me recently
    if len(not_following_back) != 0:
        file.write(f"\n{len(not_following_back)} people have unfollowed you recently. \
                Their username(s): {not_following_back}") 
    else:
        file.write(f"\nNo one has unfollowed you recently. You're good to go!")
    file.write(f"\n------------------------ Ending:[{time.strftime('%Y-%m-%d %H:%M:%S')}] ------------------------")
    file.close()
